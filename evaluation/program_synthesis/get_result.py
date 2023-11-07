import os
from collections import defaultdict
import tqdm
import jsonlines
from typing import List, Union
import itertools
import numpy as np

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

path = f'{os.environ["DUMP_FOLDER"]}/oai/prog_synthesis_n_sample_20/'
output_path = os.path.join(
    path, "reproduce_1"
)  # "eval_program_synthesis_val_execeval_fixtemp_nsampling_20_stop_at_first_fail_true",
ks = range(1, 21)


def estimate_pass_at_k(
    num_samples: Union[int, List[int], np.ndarray],
    num_correct: Union[List[int], np.ndarray],
    k: int,
) -> np.ndarray:
    """
    Estimates pass@k of each problem and returns them in an array.
    """

    def estimator(n: int, c: int, k: int):
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array(
        [estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)]
    )


def get_execeval_out_file_name(compiler):
    return os.path.join(output_path, f"{compiler}.jsonl")


# construct result as {[task_id]: [unit_test_results]}
# task_id will be src_uid_lang

pass_at_k = defaultdict(dict)

for lang, compiler in tqdm.tqdm(LANG_CLUSTER_TO_LANG_COMPILER.items()):
    execeval_out_file = get_execeval_out_file_name(compiler)
    results = defaultdict(list)
    with jsonlines.open(execeval_out_file) as jrp:
        for sample in jrp:
            src_uid = sample["source_data"]["src_uid"]
            task_id = f"{src_uid}|||{lang}"
            for ut_res in sample["unit_test_results"]:
                if "error" in ut_res:
                    continue
                results[task_id].append(ut_res)

    total, correct = [], []
    for result in results.values():
        passed = [
            all(x["exec_outcome"] == "PASSED" for x in ut_res) for ut_res in result
        ]
        total.append(len(passed))
        correct.append(sum(passed))
    total = np.array(total)
    correct = np.array(correct)

    pass_at_k[lang] = {
        f"pass@{k}": estimate_pass_at_k(total, correct, k).mean()
        for k in ks
        if (total >= k).all()
    }


langs = sorted(list(pass_at_k.keys()))
for lang in langs:
    print(f" & {lang}", end="")
print()
avg = 0
for lang in langs:
    print(f" & {round(pass_at_k[lang]['pass@5']*100, 2)}", end="")
    avg += pass_at_k[lang]["pass@5"] * 100
avg /= len(langs)
print(f" & {round(avg, 2)}")
