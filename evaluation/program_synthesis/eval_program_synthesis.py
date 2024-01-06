import os
import json
import tqdm
import jsonlines
import datasets
import concurrent.futures
from dataclasses import dataclass, field
import itertools
from collections import defaultdict

import requests
from typing import List, Optional, Union, Tuple
from enum import Enum
from multiprocessing import Pool


class ExecOutcome(Enum):
    PASSED = "PASSED"  # code executes and output matches expected output
    WRONG_ANSWER = (
        "WRONG_ANSWER"  # code executes and output does NOT matches expected output
    )
    TIME_LIMIT_EXCEEDED = "TIME_LIMIT_EXCEEDED"  # code executes and didn't exit in time, output is ignored in this case
    RUNTIME_ERROR = "RUNTIME_ERROR"  # code failed to execute (crashed)
    COMPILATION_ERROR = "COMPILATION_ERROR"  # code failed to compile
    MEMORY_LIMIT_EXCEEDED = (
        "MEMORY_LIMIT_EXCEEDED"  # code exceeded memory limit during execution
    )


@dataclass
class ExtendedUnittest:
    input: str
    output: List[str] = field(default_factory=list)
    result: Optional[str] = None
    exec_outcome: Optional[ExecOutcome] = None

    def json(self):
        _json = self.__dict__
        if self.exec_outcome is not None:
            _json["exec_outcome"] = self.exec_outcome.name

        return _json

    @classmethod
    def from_json(cls, _json):
        return cls(
            input=_json.get("input", ""),
            output=_json.get("output", list()),
            result=_json.get("result", None),
            exec_outcome=_json.get("exec_outcome", None),
        )


class EmptyValueError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EmptyUnittestError(EmptyValueError):
    pass


class EmptyLanguageError(EmptyValueError):
    pass


class EmptySourceCodeError(EmptyValueError):
    pass


class APICommunication:
    _session: requests.Session

    def __init__(self, server_url: str = "http://localhost:5000"):
        self._session = requests.Session()
        self.execute_code_url = f"{server_url}/api/execute_code"
        self.get_runtimes_url = f"{server_url}/api/all_runtimes"

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._session.close()

    def get_runtimes(self):
        return self._session.get(self.get_runtimes_url).json()

    def execute_code(
        self,
        language: str,
        source_code: str,
        unittests: List[dict],
        limits: Optional[dict] = None,
        block_network: bool = True,
        stop_on_first_fail: bool = True,
        use_sanitizer: bool = False,
        compiler_program_name: Optional[str] = None,
        compiler_flags: Optional[str] = None,
        interpreter_cmd: Optional[str] = None,
        interpreter_flags: Optional[str] = None,
        sample_id: Optional[int] = None,
        task_id: Union[str, int, None] = None,
    ) -> Tuple[List[ExtendedUnittest], Optional[int], Union[str, int, None]]:
        if language is None:
            raise EmptyLanguageError

        if source_code is None:
            raise EmptySourceCodeError

        if unittests is None or len(unittests) == 0:
            raise EmptyUnittestError

        request_body = dict(
            language=language,
            source_code=source_code,
            unittests=unittests,
            limits=limits if isinstance(limits, dict) else None,
            compile_cmd=compiler_program_name,
            compile_flags=compiler_flags,
            execute_cmd=interpreter_cmd,
            execute_flags=interpreter_flags,
            block_network=block_network,
            stop_on_first_fail=stop_on_first_fail,
            use_sanitizer=use_sanitizer,
        )
        json_response = self._session.post(
            self.execute_code_url,
            json=request_body,
            headers={"Content-Type": "application/json"},
        ).json()

        if "data" not in json_response:
            return json_response, sample_id, task_id

        return (
            json_response["data"],
            sample_id,
            task_id,
        )


def get_idx(file_name):
    return int(file_name.split(".json")[0].split("_")[0])


def sanitize_code(code):
    FLAG = True
    while FLAG == True:
        FLAG = False
        if code.startswith("```"):
            FLAG = True
            code = code.replace("```", "", 1)
        last_index = code.rfind("```")
        if last_index != -1:
            FLAG = True
            code = code[:last_index] + "" + code[last_index + len("```") :]
        if code.startswith("cpp"):
            FLAG = True
            code = code.replace("cpp", "", 1)
    return code


def fix_uts(uts):
    uts_fx = []
    for ut in uts:
        uts_fx.append(
            {
                "input": ut["input"],
                "output": ut["output"],
            }
        )
    return uts_fx


def process(args):
    sample, execeval = args
    src_uid = sample["source_data"]["src_uid"]
    unit_tests = json.loads(sample["source_data"]["hidden_unit_tests"])
    compiler = LANG_CLUSTER_TO_LANG_COMPILER[sample["source_data"]["lang_cluster"]]
    sample["unit_test_results"] = []
    for choice in sample["oai_response"]["choices"]:
        code = choice["message"]["content"]
        code = sanitize_code(code)
        unit_test_results, _, _ = execeval.execute_code(
            compiler,
            code,
            fix_uts(unit_tests),
            task_id=src_uid,
            # stop_on_first_fail=False
        )
        # print(unit_test_results)
        # print(file, code, [e['exec_outcome'] for e in unit_test_results])
        sample["unit_test_results"].append(unit_test_results)
    return sample


LANG_CLUSTER_TO_LANG_COMPILER = {
    "C": "GNU C11",
    "C#": "Mono C#",
    "C++": "GNU C++17",
    "Go": "Go",
    "Java": "Java 17",
    "Javascript": "Node.js",
    "Kotlin": "Kotlin 1.4",
    "PHP": "PHP",
    "Python": "PyPy 3",
    "Ruby": "Ruby 3",
    "Rust": "Rust 2018",
}


def main():
    path = f'{os.environ["DUMP_FOLDER"]}/oai/prog_synthesis_n_sample_20/'
    for k, debug_compiler in LANG_CLUSTER_TO_LANG_COMPILER.items():
        output_path = os.path.join(path, "reproduce_1")
        os.makedirs(output_path, exist_ok=True)
        output_file = os.path.join(output_path, f"{debug_compiler}.jsonl")
        with concurrent.futures.ThreadPoolExecutor(max_workers=129) as thread_executor:
            with jsonlines.open(output_file, "w") as jwp:
                files = sorted(os.listdir(path))
                with APICommunication(server_url="http://localhost:5000") as execeval:
                    all_samples = []
                    for file in files:
                        full_path = os.path.join(path, file)
                        if os.path.isdir(full_path):
                            continue
                        sample = json.load(open(full_path))
                        if (
                            sample["source_data"]["lang_cluster"]
                            not in LANG_CLUSTER_TO_LANG_COMPILER
                        ):
                            continue
                        compiler = LANG_CLUSTER_TO_LANG_COMPILER[
                            sample["source_data"]["lang_cluster"]
                        ]
                        if compiler != debug_compiler:
                            continue
                        all_samples.append(sample)
                    future_to_val_results = {
                        thread_executor.submit(process, args)
                        for args in itertools.product(all_samples, [execeval])
                    }

                    for _out in tqdm.tqdm(
                        concurrent.futures.as_completed(future_to_val_results),
                        total=len(all_samples),
                        desc=f"{debug_compiler}",
                    ):
                        try:
                            __out = _out.result()
                            jwp.write(__out)
                        except Exception as emsg:
                            print("Exception msg: {}".format(emsg))
                            pass


if __name__ == "__main__":
    main()
