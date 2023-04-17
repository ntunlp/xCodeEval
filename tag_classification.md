# Tag Classification Task

To download the tag classification data,

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "tag_classification/*"
git lfs pull --include "problem_descriptions.jsonl"
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
6. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved. Refer to [Structure of `problem_descriptions.jsonl`](./README.md#structure-of-problem_descriptionsjsonl)
7. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c tag_classification | md5sum
```

Output should match, `dab9c6ef6530a36319b8a8023192ce62`.


## Tree

A total of 3 directories and 133 files.

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

