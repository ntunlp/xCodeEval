# Automatic Program Repair Task

## Tree

```
code_translation/
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
├── train.jsonl
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




## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c code_translation | md5sum
```

Output should match, `1043f68a708e4557d999cd2e8547b318`.