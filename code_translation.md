# Code Translation Task

## Download data using huggingface `load_dataset()`

```
>>> import datasets
>>> code_translation_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "code_translation")
>>> print(code_translation_dataset)

DatasetDict({
    train: Dataset({
        features: ['prob_desc_memory_limit', 'prob_desc_sample_inputs', 'prob_desc_output_spec', 'file_name', 'code_uid', 'lang_cluster', 'prob_desc_sample_outputs', 'prob_desc_description', 'prob_desc_output_to', 'lang', 'prob_desc_notes', 'prob_desc_created_at', 'source_code', 'exec_outcome', 'prob_desc_input_from', 'difficulty', 'src_uid', 'prob_desc_input_spec', 'prob_desc_time_limit', 'hidden_unit_tests'],
        num_rows: 5538841
    })
    validation: Dataset({
        features: ['prob_desc_memory_limit', 'prob_desc_sample_inputs', 'prob_desc_output_spec', 'file_name', 'code_uid', 'lang_cluster', 'prob_desc_sample_outputs', 'prob_desc_description', 'prob_desc_output_to', 'lang', 'prob_desc_notes', 'prob_desc_created_at', 'source_code', 'exec_outcome', 'prob_desc_input_from', 'difficulty', 'src_uid', 'prob_desc_input_spec', 'prob_desc_time_limit', 'hidden_unit_tests'],
        num_rows: 7034
    })
    test: Dataset({
        features: ['prob_desc_memory_limit', 'prob_desc_sample_inputs', 'prob_desc_output_spec', 'file_name', 'code_uid', 'lang_cluster', 'prob_desc_sample_outputs', 'prob_desc_description', 'prob_desc_output_to', 'lang', 'prob_desc_notes', 'prob_desc_created_at', 'source_code', 'exec_outcome', 'prob_desc_input_from', 'difficulty', 'src_uid', 'prob_desc_input_spec', 'prob_desc_time_limit', 'hidden_unit_tests'],
        num_rows: 20356
    })
    validation_small: Dataset({
        features: ['prob_desc_memory_limit', 'prob_desc_sample_inputs', 'prob_desc_output_spec', 'file_name', 'code_uid', 'lang_cluster', 'prob_desc_sample_outputs', 'prob_desc_description', 'prob_desc_output_to', 'lang', 'prob_desc_notes', 'prob_desc_created_at', 'source_code', 'exec_outcome', 'prob_desc_input_from', 'difficulty', 'src_uid', 'prob_desc_input_spec', 'prob_desc_time_limit', 'hidden_unit_tests'],
        num_rows: 440
    })
})
```	
			
## Download data using git LFS

When loading with huggingface `load_dataset()` api, no need to do additional data linking. But if you are donwloading data in raw `*.jsonl` format, you need to link proper field for the task. To link the data, use `src_uid` to match row from `problem_descriptions.jsonl` and `unittest_db.json`. 

To download the code translation data,

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "code_translation/*"
git lfs pull --include "problem_descriptions.jsonl"
git lfs pull --include "unittest_db.json"
```


## A Sample from train/validation/test split

```
{
    "lang": "GNU C++11",
    "source_code": "#include<stdio.h>\nint main()\n{\n    long long n,a,b,i,maxb;\n    scanf(\"%I64d %I64d %I64d\",&n,&a,&b);\n    maxb=b;\n    long long x[n];\n    for(i=0;i<=n-1;i++)\n    {\n        scanf(\"%I64d\",&x[i]);\n    }\n    for(i=0;i<=n-1;i++)\n    {\n        if(x[i]==0)\n        {\n            if(b>0)\n                b=b-1;\n            else if(a>0)\n                a=a-1;\n        }\n        else if(x[i]==1)\n        {\n            if(a>0&&b<maxb)\n            {\n                a=a-1;\n                b=b+1;\n            }\n            else if(b>0)\n                b=b-1;\n        }\n        if(a==0&&b==0)\n            break;\n    }\n    if(i==n)\n        i=i-1;\n    printf(\"%I64d\\n\",i+1);\n    return 0;\n}//2019-10-08 13:28:20.149",
    "lang_cluster": "C++",
    "tags": [
        "greedy"
    ],
    "code_uid": "80765395fd5eb715873f3eaa3e1d36f1",
    "src_uid": "75ef1f52ef3a86992159eef566dddc89",
    "difficulty": 1500.0,
    "exec_outcome": "PASSED"
}
```


## Key Definitions

1. `lang`: Runtime/Compiler version of the `source_code`.
2. `source_code`: A program.
3. `code_uid`: A unique ID for the sample. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `code_uid`.
4. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved. Refer to [Structure of `problem_descriptions.jsonl`](./README.md#structure-of-problem_descriptionsjsonl)
5. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  
6. `exec_outcome`: Execution outcome status. Follow [Section 4.1](https://arxiv.org/pdf/2303.03004.pdf) to know the potential list of outcomes. The `exec_outcome` flags in the training data comes from a pre-run environmeent. However, training data doesn't  includes unit-test to avoid potential hacks. We provide unit test for only dev and test data.  
7. `lang_cluster`: A generic programming language name the value of `lang` belongs to.

The following keys will come from `problem_descriptions.jsonl` by matching `src_uid`,
            
8. `prob_desc_description`: Problem description in textual format, math operations are written in latex.
9. `prob_desc_input_from`: How the program should take the unit test.
10. `prob_desc_output_to`: Where the program should output the result of the unit test.
11. `prob_desc_time_limit`: Time limit to solve the problem. 
12. `prob_desc_memory_limit`: Memory limit to solve the problem.
13. `prob_desc_input_spec`: How and in what order the input will be given to the program? It also includes the date range, types, and sizes.
14. `prob_desc_output_spec`: How the outputs should be printed. Most of the time the unit test results are matched with an *exact string match* or *floating point comparison* with a precision boundary. 
15. `prob_desc_sample_inputs`: A sample input for the code that is expected to solve the problem described in `description`.
16. `prob_desc_sample_outputs`: The expected output for the `sample_input` that is expected to solve the problem described in `description`.
17. `prob_desc_notes`: Explanation of `sample_inputs` & `sample_outputs`.
18. `prob_desc_created_at`: The Unix timestamp when the problem was released. Use `datetime` lib in Python to parse it to a human-readable format.

source information will come from the name of the `*.jsonl` file name. 
19. `file_name`: Name of the source jsonl file from where data is loaded.

Unit test information will come from `unittest_db.json` by matching `src_uid`.
20. `hidden_unit_tests`: a list of unit tests returned as string. use `json.loads(hidden_unit_tests)` to load the data.

## Definition of parallelism

Dev and test data don't require parallel counterparts since the model has to generate a code segment which will be evaluated by unit-test. 
But creating training data for translation can be tricky and may require creative solutions. All the samples whose `src_uid` is the same are parallel. So if we want to take all possible pairwise data it may be extremely large. It may not be viable to train that amount of data. So the authors of this benchmark expect the users to come up with new ideas on how they can pair up solution in different programming languages. No hints for more creativity ... !!!! 

## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c code_translation | md5sum
```

Output should match, `a6e72db3f75d9d8fc3d11f7f597c7824`.


## Tree

3 directories, 133 files

```
.
├── test
│   ├── C#.jsonl
│   ├── C++.jsonl
│   ├── C.jsonl
│   ├── Go.jsonl
│   ├── Java.jsonl
│   ├── Javascript.jsonl
│   ├── Kotlin.jsonl
│   ├── PHP.jsonl
│   ├── Python.jsonl
│   ├── Ruby.jsonl
│   └── Rust.jsonl
├── train
│   ├── train_000.jsonl
│   ├── train_001.jsonl
│   ├── train_002.jsonl
│   ├── train_003.jsonl
│   ├── train_004.jsonl
│   ├── train_005.jsonl
│   ├── train_006.jsonl
│   ├── train_007.jsonl
│   ├── train_008.jsonl
│   ├── train_009.jsonl
│   ├── train_010.jsonl
│   ├── train_011.jsonl
│   ├── train_012.jsonl
│   ├── train_013.jsonl
│   ├── train_014.jsonl
│   ├── train_015.jsonl
│   ├── train_016.jsonl
│   ├── train_017.jsonl
│   ├── train_018.jsonl
│   ├── train_019.jsonl
│   ├── train_020.jsonl
│   ├── train_021.jsonl
│   ├── train_022.jsonl
│   ├── train_023.jsonl
│   ├── train_024.jsonl
│   ├── train_025.jsonl
│   ├── train_026.jsonl
│   ├── train_027.jsonl
│   ├── train_028.jsonl
│   ├── train_029.jsonl
│   ├── train_030.jsonl
│   ├── train_031.jsonl
│   ├── train_032.jsonl
│   ├── train_033.jsonl
│   ├── train_034.jsonl
│   ├── train_035.jsonl
│   ├── train_036.jsonl
│   ├── train_037.jsonl
│   ├── train_038.jsonl
│   ├── train_039.jsonl
│   ├── train_040.jsonl
│   ├── train_041.jsonl
│   ├── train_042.jsonl
│   ├── train_043.jsonl
│   ├── train_044.jsonl
│   ├── train_045.jsonl
│   ├── train_046.jsonl
│   ├── train_047.jsonl
│   ├── train_048.jsonl
│   ├── train_049.jsonl
│   ├── train_050.jsonl
│   ├── train_051.jsonl
│   ├── train_052.jsonl
│   ├── train_053.jsonl
│   ├── train_054.jsonl
│   ├── train_055.jsonl
│   ├── train_056.jsonl
│   ├── train_057.jsonl
│   ├── train_058.jsonl
│   ├── train_059.jsonl
│   ├── train_060.jsonl
│   ├── train_061.jsonl
│   ├── train_062.jsonl
│   ├── train_063.jsonl
│   ├── train_064.jsonl
│   ├── train_065.jsonl
│   ├── train_066.jsonl
│   ├── train_067.jsonl
│   ├── train_068.jsonl
│   ├── train_069.jsonl
│   ├── train_070.jsonl
│   ├── train_071.jsonl
│   ├── train_072.jsonl
│   ├── train_073.jsonl
│   ├── train_074.jsonl
│   ├── train_075.jsonl
│   ├── train_076.jsonl
│   ├── train_077.jsonl
│   ├── train_078.jsonl
│   ├── train_079.jsonl
│   ├── train_080.jsonl
│   ├── train_081.jsonl
│   ├── train_082.jsonl
│   ├── train_083.jsonl
│   ├── train_084.jsonl
│   ├── train_085.jsonl
│   ├── train_086.jsonl
│   ├── train_087.jsonl
│   ├── train_088.jsonl
│   ├── train_089.jsonl
│   ├── train_090.jsonl
│   ├── train_091.jsonl
│   ├── train_092.jsonl
│   ├── train_093.jsonl
│   ├── train_094.jsonl
│   ├── train_095.jsonl
│   ├── train_096.jsonl
│   ├── train_097.jsonl
│   ├── train_098.jsonl
│   ├── train_099.jsonl
│   ├── train_100.jsonl
│   ├── train_101.jsonl
│   ├── train_102.jsonl
│   ├── train_103.jsonl
│   ├── train_104.jsonl
│   ├── train_105.jsonl
│   ├── train_106.jsonl
│   ├── train_107.jsonl
│   ├── train_108.jsonl
│   ├── train_109.jsonl
│   └── train_110.jsonl
└── validation
    ├── C#.jsonl
    ├── C++.jsonl
    ├── C.jsonl
    ├── Go.jsonl
    ├── Java.jsonl
    ├── Javascript.jsonl
    ├── Kotlin.jsonl
    ├── PHP.jsonl
    ├── Python.jsonl
    ├── Ruby.jsonl
    └── Rust.jsonl
```
