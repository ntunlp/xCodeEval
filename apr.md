# Automatic Program Repair Task

## Tree

```
apr
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

## A Sample from train split
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

## A Sample from validation/test split

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


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c apr | md5sum
```

Output should match, `044963b52e550292a4dee5e4c63e3fce`.