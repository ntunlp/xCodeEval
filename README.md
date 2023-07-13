# xCodeEval
[xCodeEval: A Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval](https://arxiv.org/abs/2303.03004)

# Update:
- July 13, 2023: StarEncode retrieval model released. [Follow it here](#additional-resources)
- Jul 6, 2023: [ExecEval](https://github.com/ntunlp/ExecEval) has been updated with changes for java, kotlin, go. Please `git pull`, `docker build`, `docker run` for latest updates.


We introduce **xCodeEval**, the largest executable multilingual multitask benchmark to date consisting of 25 M document-level coding examples from about 7.5K unique problems covering up to 17 programming languages with execution-level parallelism. It features a total of seven tasks involving code understanding, generation, translation and retrieval, and it employs an execution-based evaluation. We develop a test-case based multilingual code execution engine, [**ExecEval**](https://github.com/ntunlp/ExecEval) that supports all the programming languages in **xCodeEval**. We also propose a novel data splitting and a data selection schema for balancing data distributions over multiple attributes based on geometric mean and graph-theoretic principle. 

This repository contains the sample code and data link for xCodeEval [paper](https://arxiv.org/abs/2303.03004).

# Data Download

[Huggingface-dataset](https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval)

Currently this repository supports huggingface [`load_dataset()`](https://huggingface.co/docs/datasets/v1.11.0/package_reference/loading_methods.html#datasets.load_dataset) api. Follow the following example to load dataset for individual examples. 

```
import datasets

prog_synthesis_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "program_synthesis")
code_translation_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "code_translation")
tag_classification_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "tag_classification")
apr_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "apr")
pcode_compilation_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "code_compilation")
retrieval_code_code_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "retrieval_code_code")
retrieval_nl_code_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "retrieval_nl_code")
retrieval_corpus_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "retrieval_corpus")

```

## Hf large data download tricks.


If you are facing long delay with data processing, add a `ignore_verifications=True`.

```
prog_synthesis_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "program_synthesis", ignore_verifications=True)
```

If you are facing long delay with data downloading, use huggingface streaming mode.

```
prog_synthesis_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "program_synthesis", streaming=True)
```

## Just Give me the raw data (😠)

Data can be also downloaded as a git LFS repo from huggingface. 

![xCodeEval_hf](https://github.com/ntunlp/xCodeEval/blob/main/xcodeeval-hf.png?raw=true)

You can download the full data using the following command.

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull
```

To download a specific part of the dataset, 

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "apr/test/*"
```

We propose 7 Tasks.

1. [Tag Classification](./tag_classification.md)
2. [Code Compilation](./code_compilation.md)
3. [Program Synthesis](./program_synthesis.md)
4. [Code Translation](./code_translation.md)
5. [Automatic Program Repair](./apr.md)
6. [Code-Code Retrieval](./retrieval.md)
7. [NL-Code Retrieval](./retrieval.md)

# Common Data for different tasks

![xCodeEval_fig_1](xcodeeval_fig_1.png)

We have two data files that are required for multiple tasks.

1. `problem_descriptions.jsonl`
2. `unittest_db.json`

You can find these two files in the root directory of the [main](https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval/tree/main) branch of huggingface dataset repository. To avoid data redundancy we didn't include these data with the relevant tasks, rather we add a unique id `src_uid` to retrieve these data. 

## Structure of `problem_descriptions.jsonl`

A sample, 

```json
{
    "description": "There are $$$n$$$ positive integers $$$a_1, a_2, \\dots, a_n$$$. For the one move you can choose any even value $$$c$$$ and divide by two all elements that equal $$$c$$$.For example, if $$$a=[6,8,12,6,3,12]$$$ and you choose $$$c=6$$$, and $$$a$$$ is transformed into $$$a=[3,8,12,3,3,12]$$$ after the move.You need to find the minimal number of moves for transforming $$$a$$$ to an array of only odd integers (each element shouldn't be divisible by $$$2$$$).",
    "input_from": "standard input",
    "output_to": "standard output",
    "time_limit": "3 seconds",
    "memory_limit": "256 megabytes",
    "input_spec": "The first line of the input contains one integer $$$t$$$ ($$$1 \\le t \\le 10^4$$$) \u2014 the number of test cases in the input. Then $$$t$$$ test cases follow. The first line of a test case contains $$$n$$$ ($$$1 \\le n \\le 2\\cdot10^5$$$) \u2014 the number of integers in the sequence $$$a$$$. The second line contains positive integers $$$a_1, a_2, \\dots, a_n$$$ ($$$1 \\le a_i \\le 10^9$$$). The sum of $$$n$$$ for all test cases in the input doesn't exceed $$$2\\cdot10^5$$$.",
    "output_spec": "For $$$t$$$ test cases print the answers in the order of test cases in the input. The answer for the test case is the minimal number of moves needed to make all numbers in the test case odd (i.e. not divisible by $$$2$$$).",
    "notes": "NoteIn the first test case of the example, the optimal sequence of moves can be as follows:  before making moves $$$a=[40, 6, 40, 3, 20, 1]$$$;  choose $$$c=6$$$;  now $$$a=[40, 3, 40, 3, 20, 1]$$$;  choose $$$c=40$$$;  now $$$a=[20, 3, 20, 3, 20, 1]$$$;  choose $$$c=20$$$;  now $$$a=[10, 3, 10, 3, 10, 1]$$$;  choose $$$c=10$$$;  now $$$a=[5, 3, 5, 3, 5, 1]$$$ \u2014 all numbers are odd. Thus, all numbers became odd after $$$4$$$ moves. In $$$3$$$ or fewer moves, you cannot make them all odd.",
    "sample_inputs": [
        "4\n6\n40 6 40 3 20 1\n1\n1024\n4\n2 4 8 16\n3\n3 1 7"
    ],
    "sample_outputs": [
        "4\n10\n4\n0"
    ],
    "tags": [
        "number theory",
        "greedy"
    ],
    "src_uid": "afcd41492158e68095b01ff1e88c3dd4",
    "difficulty": 1200,
    "created_at": 1576321500
}
```

### Key Definitions

1. `description`: Problem description in textual format, math operations are written in latex.
2. `input_from`: How the program should take the unit test.
3. `output_to`: Where the program should output the result of the unit test.
4. `time_limit`: Time limit to solve the problem. 
5. `memory_limit`: Memory limit to solve the problem.
6. `input_spec`: How and in what order the input will be given to the program? It also includes the date range, types, and sizes.
7. `output_spec`: How the outputs should be printed. Most of the time the unit test results are matched with an *exact string match* or *floating point comparison* with a precision boundary. 
8. `sample_inputs`: A sample input for the code that is expected to solve the problem described in `description`.
9. `sample_outputs`: The expected output for the `sample_input` that is expected to solve the problem described in `description`.
10. `notes`: Explanation of `sample_inputs` & `sample_outputs`.
11. `tags`: The problem categories.
12. `src_uid`: The unique id of the problem. This ID is referred to in the task data samples instead of putting all this information.
13. `difficulty`: How difficult is it to solve the problem for a human (annotated by an expert human)? 
14. `created_at`: The Unix timestamp when the problem was released. Use `datetime` lib in Python to parse it to a human-readable format.  

## Structure of `unittest_db.json`

The structure of the `json` file, 

```python
unittest_db = {
	"db884d679d9cfb1dc4bc511f83beedda" : [
		{
			"input": "4\r\n3 2 3 2\r\n",
			"output": [
				"1"
			],
		},
		{
			...
		},
		...
	]
	"3bc096d8cd3418948d5be6bf297aa9b5":[
		...
	],
	...
}
```

### Key Definitions

1. `unittest_db.json` dict keys i.e., `db884d679d9cfb1dc4bc511f83beedda` are the `src_uid` from `problem_descriptions.jsonl`.
2. `input`: Input of the unit test.
3. `output`: List of expected outputs for the unit test. 


# Additional Resources

1. **nl-code**: [NTU-NLP-sg/xCodeEval-nl-code-starencoder-ckpt-37](https://huggingface.co/NTU-NLP-sg/xCodeEval-nl-code-starencoder-ckpt-37)
2. **code-code**: [NTU-NLP-sg/xCodeEval-code-code-starencoder-ckpt-37](https://huggingface.co/NTU-NLP-sg/xCodeEval-code-code-starencoder-ckpt-37)


# License

This repository is under [MIT](https://github.com/ntunlp/xCodeEval/blob/main/LICENSE) license. But the data is distributes through [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.

# Citation

```
@misc{khan2023xcodeeval,
      title={xCodeEval: A Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval}, 
      author={Mohammad Abdullah Matin Khan and M Saiful Bari and Xuan Long Do and Weishi Wang and Md Rizwan Parvez and Shafiq Joty},
      year={2023},
      eprint={2303.03004},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
