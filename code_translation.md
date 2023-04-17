# Automatic Program Repair Task

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

## Definition of parallelism

Dev and test data don't require parallel counterparts since the model has to generate a code segment which will be evaluated by unit-test. 
But creating training data for translation can be tricky and may require creative solutions. All the samples whose `src_uid` is the same are parallel. So if we want to take all possible pairwise data it may be extremely large. It may not be viable to train that amount of data. So the authors of this benchmark expect the users to come up with new ideas on how they can pair up solution in different programming languages. No hints for more creativity ... !!!! 

## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c code_translation | md5sum
```

Output should match, `801a19dd92e8e9a201ad12942ec4a77e`.


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