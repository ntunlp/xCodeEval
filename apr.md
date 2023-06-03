# Automatic Program Repair (APR) Task

## Download data using huggingface `load_dataset()`

```
>>> import datasets
>>> apr_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "apr")
>>> print(apr_dataset)

DatasetDict({
    train: Dataset({
        features: ['prob_desc_output_spec', 'prob_desc_sample_outputs', 'fix_exec_outcome', 'prob_desc_sample_inputs', 'similarity_score', 'prob_desc_memory_limit', 'difficulty', 'lang', 'apr_id', 'tags', 'potential_dominant_fix_op', 'prob_desc_output_to', 'prob_desc_input_from', 'src_uid', 'bug_exec_outcome', 'lang_cluster', 'prob_desc_input_spec', 'fix_source_code', 'delete_cnt', 'prob_desc_time_limit', 'bug_code_uid', 'file_name', 'prob_desc_created_at', 'fix_ops_cnt', 'fix_code_uid', 'prob_desc_notes', 'equal_cnt', 'bug_source_code', 'prob_desc_description', 'replace_cnt', 'hidden_unit_test'],
        num_rows: 4672070
    })
    validation: Dataset({
        features: ['prob_desc_output_spec', 'prob_desc_sample_outputs', 'fix_exec_outcome', 'prob_desc_sample_inputs', 'similarity_score', 'prob_desc_memory_limit', 'difficulty', 'lang', 'apr_id', 'tags', 'potential_dominant_fix_op', 'prob_desc_output_to', 'prob_desc_input_from', 'src_uid', 'bug_exec_outcome', 'lang_cluster', 'prob_desc_input_spec', 'fix_source_code', 'delete_cnt', 'prob_desc_time_limit', 'bug_code_uid', 'file_name', 'prob_desc_created_at', 'fix_ops_cnt', 'fix_code_uid', 'prob_desc_notes', 'equal_cnt', 'bug_source_code', 'prob_desc_description', 'replace_cnt', 'hidden_unit_test'],
        num_rows: 5068
    })
    test: Dataset({
        features: ['prob_desc_output_spec', 'prob_desc_sample_outputs', 'fix_exec_outcome', 'prob_desc_sample_inputs', 'similarity_score', 'prob_desc_memory_limit', 'difficulty', 'lang', 'apr_id', 'tags', 'potential_dominant_fix_op', 'prob_desc_output_to', 'prob_desc_input_from', 'src_uid', 'bug_exec_outcome', 'lang_cluster', 'prob_desc_input_spec', 'fix_source_code', 'delete_cnt', 'prob_desc_time_limit', 'bug_code_uid', 'file_name', 'prob_desc_created_at', 'fix_ops_cnt', 'fix_code_uid', 'prob_desc_notes', 'equal_cnt', 'bug_source_code', 'prob_desc_description', 'replace_cnt', 'hidden_unit_test'],
        num_rows: 17699
    })
})
```


## Download data using git LFS

When loading with huggingface `load_dataset()` api, no need to do additional data linking. But if you are donwloading data in raw `*.jsonl` format, you need to link proper field for the task. To link the data, use `src_uid` to match row from `problem_descriptions.jsonl` and `unittest_db.json`. 


To download the automatic program repair data,

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "apr/*"
git lfs pull --include "problem_descriptions.jsonl"
git lfs pull --include "unittest_db.json"
```



## A Sample of raw data from train split (without linking)
```
{
    "similarity_score": 0.6323809523809524,
    "equal_cnt": 30,
    "replace_cnt": 8,
    "delete_cnt": 0,
    "insert_cnt": 21,
    "fix_ops_cnt": 29,
    "bug_source_code": "#include<iostream>\r\n\r\nusing namespace std;\r\nint main()\r\n{\r\n\tlong long int t;\r\n\tcin>>t;\r\n\twhile(t--)\r\n\t{\r\n\t\tlong long int n,co;co=0;\r\n\t\tcin>>n;long long int yy=0;long long int mm=0;\r\n\t\tlong long int s[n],b[n],c[n];\r\n\t\tfor (long long int i = 0; i < n; i++)\r\n\t\t{\r\n\t\t\tcin>>s[i];\r\n\t\t\tb[i]=s[i];\r\n\t\t\tc[i]=s[i];\r\n\t\t\tif(yy==0){if(c[i]==0)\r\n\t\t\t{\r\n\t\t\t\tc[i]=1;yy=1;\r\n\t\t\t}\r\n\t\t}\r\n}\r\n\t\tlong long int l;\r\n\t\tmm=0;\r\n\t\tfor (long long int i = n-1; i>=0; i--)\r\n\t\t{\r\n\t\t\tif(b[i]==1)\r\n\t\t\t{\r\n\t\t\t\tb[i]=0;l=i;break;\r\n\t\t\t}mm++;\r\n\t\t}\r\n\t\tlong long int j=0;long long int m=0;long long int op=0;long long int po=0;\r\n\t\tfor (long long int i = 0; i < n; i++)\r\n\t\t{\r\n\t\t\tj=m;\r\n\t\t\tfor (; j < n; j++)\r\n\t\t\t{\r\n\t\t\t\tif(s[i]>s[j])\r\n\t\t\t\t{\r\n\t\t\t\t\tco++;\r\n\t\t\t\t}if(b[i]>b[j])\r\n\t\t\t\t{\r\n\t\t\t\t\top++;\r\n\t\t\t\t}\t\r\n\t\t\t\tif(c[i]>c[j])\r\n\t\t\t\t{\r\n\t\t\t\t\tpo++;\r\n\t\t\t\t}\t\r\n\t\t\t}m++;\r\n\t\t}\r\n\t\tlong long int big = co > po ? (co > op ? co : op) : (po > op ? po : op) ;\r\n\tcout<<big<<endl;\r\n\t}\r\n}",
    "fix_source_code": "#include<iostream>\r\n\r\nusing namespace std;\r\nint main()\r\n{\r\n\tlong long int t;\r\n\tcin>>t;\r\n\twhile(t--)\r\n\t{\r\n\t\tlong long int n,co;co=0;\r\n\t\tcin>>n;long long int yy=0;long long int mm=0;\r\n\t\tlong long int s[n],b[n],c[n],s1[n+2],b1[n+2],c1[n+2];s1[0]=0;b1[0]=0;c1[0]=0;c1[n+1]=0;b1[n+1]=0;s1[n+1]=0;s1[1]=0;b1[1]=0;c1[1]=0;\r\n\t\tfor (long long int i = 0; i < n; i++)\r\n\t\t{\r\n\t\t\t// s1[i+1]=0;b1[i+1]=0;c1[i+1]=0;\r\n\t\t\tcin>>s[i];s1[i+1]=s1[i]+s[i];\r\n\t\t\tb[i]=s[i];\r\n\t\t\tc[i]=s[i];\r\n\t\t\tif(yy==0)\r\n\t\t\t{\r\n\t\t\t\t\tif(c[i]==0)\r\n\t\t\t\t{\r\n\t\t\t\t\tc[i]=1;yy=1;\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t\t\tc1[i+1]=c1[i]+c[i];\r\n\t\t\t\r\n\t\t\t\t\r\n\t\t}\r\n\t\tlong long int l;\r\n\t\tmm=0;\r\n\t\tfor (long long int i = n-1; i>=0; i--)\r\n\t\t{\r\n\t\t\tif(b[i]==1)\r\n\t\t\t{\r\n\t\t\t\tb[i]=0;l=i;break;\r\n\t\t\t}mm++;\r\n\t\t}\r\n\t\tfor (int i = 0; i < n; ++i)\r\n\t\t{\r\n\t\t\tb1[i+1]=b1[i]+b[i];\r\n\t\t}\r\n\t\tlong long int j=0;long long int m=0;long long int op=0;long long int po=0;\r\n\t\tfor (int i = 0; i < n; ++i)\r\n\t\t{\r\n\t\t\tif(s[i]==1){co=co-(s1[n]-s1[i+1])+n-i-1;}//\r\n\t\t\tif(b[i]==1){po=po-b1[n]+b1[i+1]+n-i-1;}\r\n\t\t\tif(c[i]==1){op=op-c1[n]+c1[i+1]+n-i-1;}//cout<<b1[i+1]<<' ';//cout<<c1[i+1]<<\"..\";\r\n\t\t}//cout<<endl<<\"ggggggggggggg\";\r\n\t\t//long long int j=0;long long int m=0;long long int op=0;long long int po=0;\r\n\t\t// for (long long int i = 0; i < n; i++)\r\n\t\t// {\r\n\t\t// \tj=m;\r\n\t\t// \tfor (; j < n; j++)\r\n\t\t// \t{\r\n\t\t// \t\tif(s[i]>s[j])\r\n\t\t// \t\t{\r\n\t\t// \t\t\tco++;\r\n\t\t// \t\t}if(b[i]>b[j])\r\n\t\t// \t\t{\r\n\t\t// \t\t\top++;\r\n\t\t// \t\t}\t\r\n\t\t// \t\tif(c[i]>c[j])\r\n\t\t// \t\t{\r\n\t\t// \t\t\tpo++;\r\n\t\t// \t\t}\t\r\n\t\t// \t}m++;\r\n\t\t// }\r\n\t\t// for (int i = 0; i < n; ++i)\r\n\t\t// {\r\n\t\t// \t code cout<<b[i]<<\" \";\r\n\t\t// }cout<<endl;\r\n\t\t// cout<<co<<\" \"<<po<<\" \"<<op<<endl;\r\n\t\tlong long int big = co > po ? (co > op ? co : op) : (po > op ? po : op) ;\r\n\tcout<<big<<endl;\r\n\t}\r\n}",
    "lang": "GNU C++14",
    "fix_code_uid": "6a3da16df80126444491ff82db4c2f48",
    "bug_code_uid": "f0839fcb69ad44dd4746e57744463718",
    "src_uid": "0657ce4ce00addefc8469381c57294fc",
    "apr_id": "dbc2dc665b753d13a31aad763426c39b",
    "difficulty": 1100,
    "tags": [
        "data structures",
        "greedy",
        "math"
    ],
    "bug_exec_outcome": "TIME_LIMIT_EXCEEDED",
    "fix_exec_outcome": "PASSED",
    "potential_dominant_fix_op": "insert",
    "lang_cluster": "C++"
}
```

## A Sample of raw data from validation/test split (without linking)

```
{
    "similarity_score": 0.9992970123022847,
    "equal_cnt": 3,
    "replace_cnt": 2,
    "delete_cnt": 0,
    "insert_cnt": 0,
    "fix_ops_cnt": 2,
    "bug_source_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct aho {\n    int go[2], link, back;\n};\n\naho suf[1600], pr[40];\nstring sufs[1600], prs[40];\n\nvoid add_string(aho m[], string ms[], int &top, string s) {\n    int u = 0;\n    for (int i = 0; i < s.size(); ++i) {\n        if (m[u].go[s[i]] == 0) {\n            ++top;\n            m[u].go[s[i]] = top;\n            ms[top] = ms[u] + s[i];\n        }\n        u = m[u].go[s[i]];\n    }\n}\n\nvoid build_aho(aho m[]) {\n    m[0].link = 0;\n    vector <int> v = {0};\n    for (int i = 0; i < v.size(); ++i) {\n        for (int j = 0; j < 2; ++j)\n        if (m[v[i]].go[j] != 0) {\n            if (i == 0)\n                m[m[v[i]].go[j]].link = 0;\n            else\n                m[m[v[i]].go[j]].link = m[m[v[i]].link].go[j];\n            v.push_back(m[v[i]].go[j]);\n        } else\n            m[v[i]].go[j] = m[m[v[i]].link].go[j];\n    }\n}\nint find_string(aho m[], string s) {\n    int u = 0;\n    for (int i = 0; i < s.size(); ++i)\n        u = m[u].go[s[i]];\n    return u;\n}\n\nstring cnt(string s) {\n    for (int i = 0; i < s.size(); ++i)\n        s[i] += '0';\n    return s;\n}\n\nlong long dp[41][41][1600][2];\n\nint main() {\n    int i, j, k, n, top, l;\n    string s;\n    //freopen(\"input.txt\", \"r\", stdin);\n    //freopen(\"output.txt\", \"w\", stdout);\n    //ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);\n    cin >> n;\n    cin >> s;\n    for (i = 0; i < s.size(); ++i)\n        s[i] -= '0';\n    if (s.size() > n) {\n        for (i = 0; i < s.size() - n; ++i)\n        if (s[i] != s[i + n]) {\n            cout << 0;\n            return 0;\n        }\n        cout << 1;\n        return 0;\n    }\n    add_string(pr, prs, j = 0, s);\n    build_aho(pr);\n    k = 0;\n    for (int i = 0; i < s.size(); ++i) {\n        string s1 = \"\";\n        for (int j = i; j < s.size(); ++j)\n            s1 += s[j];\n        add_string(suf, sufs, k, s1);\n    }\n    build_aho(suf);\n    dp[0][0][0][0] = 1;\n    for (i = 0; i < n; ++i)\n    for (j = 0; j < s.size(); ++j)\n    for (l = 0; l <= k; ++l)\n    if (l != s.size()) {\n        for (int i1 = 0; i1 < 2; ++i1)\n            dp[i + 1][pr[j].go[i1]][l][1] += dp[i][j][l][1];\n        for (int i1 = 0; i1 < 2; ++i1)\n        if (sufs[suf[l].go[i1]].size() <= sufs[l].size())\n            dp[i + 1][pr[j].go[i1]][l][1] += dp[i][j][l][0];\n        else {\n            dp[i + 1][pr[j].go[i1]][suf[l].go[i1]][0] += dp[i][j][l][0];\n        }\n    }\n    long long ans = 1;\n    for (i = 0; i < n; ++i)\n        ans *= 2;\n    for (i = 0; i <= s.size(); ++i)\n    for (j = 0; j <= k; ++j) {\n        string s1 = prs[i] + sufs[j];\n        int u = 0;\n        bool flag = true;\n        for (l = 0; l < s1.size(); ++l) {\n            u = suf[u].go[s1[l]];\n            if (u == s.size())\n                flag = false;\n        }\n        if (flag)\n            ans -= dp[n][i][j][0] + dp[n][i][j][1];\n    }\n    cout << ans;\n}\n",
    "lang": "GNU C++17",
    "bug_code_uid": "b272efc49e5fe8e487b835410c053bc8",
    "src_uid": "0034806908c9794086736a2d07fc654c",
    "apr_id": "6f93ba2ec792482a3d847a0800a20e52",
    "difficulty": 2900,
    "tags": [
        "dp",
        "strings"
    ],
    "bug_exec_outcome": "MEMORY_LIMIT_EXCEEDED",
    "potential_dominant_fix_op": "replace",
    "lang_cluster": "C++"
}
```

## Key Definitions

1. `similarity_score`: A similarity score between `bug_source_code` and `fix_source_code` given by `difflib`.
2. `equal_cnt`: A metric comparing `bug_source_code` and `fix_source_code`. Recommended by `difflib`.
3. `replace_cnt`: A metric comparing `bug_source_code` and `fix_source_code`. Recommended by `difflib`.
4. `delete_cnt`: A metric comparing `bug_source_code` and `fix_source_code`. Recommended by `difflib`.
5. `insert_cnt`: A metric comparing `bug_source_code` and `fix_source_code`. Recommended by `difflib`.
6. `fix_ops_cnt`: A metric comparing `bug_source_code` and `fix_source_code`. Recommended by `difflib`.
7. `bug_source_code`: Buggy code.
8. `fix_source_code`: A potential fix of the buggy code that passed all the unit tests.
9. `lang`: Runtime/Compiler version of the `source_code`.
10. `fix_code_uid`: A unique ID for the fix code. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `fix_code_uid`.
11. `bug_code_uid`: A unique ID for the buggy code. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `bug_code_uid`.
12. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved. Refer to [Structure of `problem_descriptions.jsonl`](./README.md#structure-of-problem_descriptionsjsonl)
13. `apr_id`: A unique ID for the apr sample. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `apr_id`.
14. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  
15. `tags`: List of potential algorithmic techniques required to write the program.
16. `bug_exec_outcome`: A pre-run execution outcome of `bug_source_code`. Follow [Section 4.1](https://arxiv.org/pdf/2303.03004.pdf) to know the potential list of outcomes. The `exec_outcome` flags in the training data comes from a pre-run environmeent. However, training data doesn't  includes unit-test to avoid potential hacks. We provide unit test for only dev and test data.   
17. `fix_exec_outcome`: A pre-run execution outcome of `fix_source_code`. Follow [Section 4.1](https://arxiv.org/pdf/2303.03004.pdf) to know the potential list of outcomes. The `exec_outcome` flags in the training data comes from a pre-run environmeent. However, training data doesn't  includes unit-test to avoid potential hacks. We provide unit test for only dev and test data.   
18. `potential_dominant_fix_op`: A potential fix op recommended by difflib.
19. `lang_cluster`: A generic programming language name the value of `lang` belongs to.

## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c apr | md5sum
```

Output should match, `5cba33fa21d64cf3ba190744ab49f0da`.


## Tree

3 directories, 116 files

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
│   └── train_093.jsonl
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