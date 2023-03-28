# Code Compilation Task

## Tree

```
tag_classification/
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
    "lang": "GNU C++17",
    "source_code": "#include<bits/stdc++.h>\nusing namespace std;\nchar s[200005],t[200005];\nint s1[200005],t1[200005];\nint n;\nint main()\n{\n    cin>>n;\n    cin>>s+1>>t+1;\n    for(int i=1; i<=n; i++)\n        s1[n+1-i]=s[i]-'a'+1,t1[n+1-i]=t[i]-'a'+1;\n\n    for(int i=1; i<=n; i++)\n        s1[i]+=t1[i];\n\n    for(int i=1; i<=n; i++)\n    {\n        if(s1[i]>=26)\n        {\n            s1[i]%=26;\n            s1[i+1]+=1;\n        }\n    }\n\n    if(s1[n+1]) s1[n]+=26;\n\n\n    for(int i=1; i<=n; i++)\n    {\n        if(!s1[i])\n        {\n            s1[i+1]--;\n            s1[i]=26;\n        }\n        if(s1[i]&1)\n            s1[i-1]+=26;\n\n    }\n    for(int i=1; i<=n; i++)\n    {\n        s1[i]/=2;\n        if(s1[i]==0)\n            s1[i]=26,s1[i+1]--;\n    }\n\n    for(int i=n; i>=1; i--)\n        printf(\"%c\",'a'-1+s1[i]);\n\n    return 0;\n}\n",
    "lang_cluster": "C++",
    "compilation_error": false,
    "code_uid": "c6afb1328299497e14ac949dbe60d038",
    "src_uid": "5f4009d4065f5ad39e662095f8f5c068",
    "difficulty": 1900
}
```
 
## Key Definitions


1. `lang`: Runtime/Compiler version of the `source_code`.
2. `source_code`: A program.
3. `lang_cluster`: A generic programming language name the value of `lang` belongs to.
4. `compilation_error`: True/False, Indicates if the code generates a compilation error or not.
5. `code_uid`: A unique ID for the sample. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `code_uid`.
6. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved.
7. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c code_compilation | md5sum
```

Output should match, `a03d252b4a58451d1e118b3e80d8a3f3`.