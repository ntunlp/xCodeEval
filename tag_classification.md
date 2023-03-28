# Tag Classification Task

## Tree

```
ag_classification/
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

## train/validation/test split
```
{
    "lang": "GNU C++17",
    "source_code": "#include <bits/stdc++.h>\n#include <chrono> \nusing namespace std::chrono; \n\nusing namespace std;\n#define f0r(a, b) for (a = 0; a < b; a++)\n#define f1r(a, b, c) for (a = b; a < c; a++)\n#define ms(arr, v) memset(arr, v, sizeof(arr))\n#define pb push_back\n#define io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)\n#define mp make_pair\n#define f first\n#define s second\ntypedef long long ll;\ntypedef double ld;\ntypedef pair<int, int> pii;\ntypedef pair<ll, ll> pll;\nll i, j;\n\nll n, q, Q, T, m, k, r, x, y, z, g;\nstring a, b;\nunsigned char ans[200001];\n\nint main() {\n  io;\n  cin >> n >> a >> b;\n  ms(ans, 0);\n  for (int i = n-1; i >= 0; i--) {\n    // f0r(j, n) cout << (char)(ans[j] < 10 ? ans[j] + '0' : ans[j]);\n    cout << endl;\n    if (i == n-1) {\n      if (a[i] > b[i]) {\n        int diff = a[i] - b[i];\n        int x = b[i] + (diff>>1);\n        while (x > 'z') {\n          x -= 26;\n          ans[i-1]++;\n        }\n        ans[i] = x;\n      } else {\n        int diff = b[i] - a[i];\n        int x = a[i] + (diff>>1);\n        ans[i] = x;\n      }\n      continue;\n    }\n    if (a[i] < b[i]) {\n      int diff = b[i] - a[i];\n      ans[i] += a[i] + (diff>>1);\n      if (diff % 2 != 0) {\n        ans[i+1] += 13;\n        while (ans[i+1] > 'z') {\n          ans[i+1] -= 26;\n          ans[i]++;\n        }\n      }\n      while (ans[i] > 'z') {\n        ans[i] -= 26;\n        ans[i-1]++;\n      }\n    } else if (a[i] == b[i]) {\n      ans[i] = a[i];\n    } else {\n      int diff = a[i] - b[i];\n      ans[i] += b[i] + (diff>>1);\n      if (diff % 2 != 0) {\n        ans[i+1] += 13;\n        while (ans[i+1] > 'z') {\n          ans[i+1] -= 26;\n          ans[i]++;\n        }\n      }\n      while (ans[i] > 'z') {\n        ans[i] -= 26;\n        ans[i-1]++;\n      }\n    }\n  }\n  f0r(i, n) cout << ans[i];\n  cout << endl;\n  // cout << \"FLUSH PLEASE\" << endl;\n}",
    "tags": [
        "bitmasks",
        "strings",
        "number theory",
        "math"
    ],
    "lang_cluster": "C++",
    "code_uid": "d215a290b8ae7055870ec4fb61218286",
    "src_uid": "5f4009d4065f5ad39e662095f8f5c068",
    "difficulty": 1900
}
```

## Key Definitions


1. `lang`: Runtime/Compiler version of the `source_code`.
2. `source_code`: A program.
3. `tags`: List of potential algorithmic techniques required to write the program.
4. `lang_cluster`: A generic programming language name the value of `lang` belongs to.
5. `code_uid`: A unique ID for the sample. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `code_uid`.
6. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved.
7. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c tag_classification | md5sum
```

Output should match, `0fa93074af9be58156919cb71ba90534`.