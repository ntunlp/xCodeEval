# Program Synthesis Task

To download the program synthesis data,

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "program_synthesis/*"
git lfs pull --include "problem_descriptions.jsonl"
git lfs pull --include "unittest_db.json"
```


## A Sample from train split

```
{
  "lang": "GNU C++17",
  "source_code": "#include <bits/stdc++.h>\n#include <chrono> \nusing namespace std::chrono; \n\nusing namespace std;\n#define f0r(a, b) for (a = 0; a < b; a++)\n#define f1r(a, b, c) for (a = b; a < c; a++)\n#define ms(arr, v) memset(arr, v, sizeof(arr))\n#define pb push_back\n#define io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)\n#define mp make_pair\n#define f first\n#define s second\ntypedef long long ll;\ntypedef double ld;\ntypedef pair<int, int> pii;\ntypedef pair<ll, ll> pll;\nll i, j;\n\nll n, q, Q, T, m, k, r, x, y, z, g;\nstring a, b;\nunsigned char ans[200001];\n\nint main() {\n  io;\n  cin >> n >> a >> b;\n  ms(ans, 0);\n  for (int i = n-1; i >= 0; i--) {\n    // f0r(j, n) cout << (char)(ans[j] < 10 ? ans[j] + '0' : ans[j]);\n    cout << endl;\n    if (i == n-1) {\n      if (a[i] > b[i]) {\n        int diff = a[i] - b[i];\n        int x = b[i] + (diff>>1);\n        while (x > 'z') {\n          x -= 26;\n          ans[i-1]++;\n        }\n        ans[i] = x;\n      } else {\n        int diff = b[i] - a[i];\n        int x = a[i] + (diff>>1);\n        ans[i] = x;\n      }\n      continue;\n    }\n    if (a[i] < b[i]) {\n      int diff = b[i] - a[i];\n      ans[i] += a[i] + (diff>>1);\n      if (diff % 2 != 0) {\n        ans[i+1] += 13;\n        while (ans[i+1] > 'z') {\n          ans[i+1] -= 26;\n          ans[i]++;\n        }\n      }\n      while (ans[i] > 'z') {\n        ans[i] -= 26;\n        ans[i-1]++;\n      }\n    } else if (a[i] == b[i]) {\n      ans[i] = a[i];\n    } else {\n      int diff = a[i] - b[i];\n      ans[i] += b[i] + (diff>>1);\n      if (diff % 2 != 0) {\n        ans[i+1] += 13;\n        while (ans[i+1] > 'z') {\n          ans[i+1] -= 26;\n          ans[i]++;\n        }\n      }\n      while (ans[i] > 'z') {\n        ans[i] -= 26;\n        ans[i-1]++;\n      }\n    }\n  }\n  f0r(i, n) cout << ans[i];\n  cout << endl;\n  // cout << \"FLUSH PLEASE\" << endl;\n}",
  "tags": [
    "number theory",
    "bitmasks",
    "math",
    "strings"
  ],
  "lang_cluster": "C++",
  "src_uid": "5f4009d4065f5ad39e662095f8f5c068",
  "code_uid": "3a1d3fab20424f3fadea46e0ac60f0c6",
  "difficulty": 1900,
  "exec_outcome": "PASSED"
}
```

## A Sample from validation/test split
```
{
  "description": "You are given a string $$$s$$$ consisting of lowercase Latin letters. Let the length of $$$s$$$ be $$$|s|$$$. You may perform several operations on this string.In one operation, you can choose some index $$$i$$$ and remove the $$$i$$$-th character of $$$s$$$ ($$$s_i$$$) if at least one of its adjacent characters is the previous letter in the Latin alphabet for $$$s_i$$$. For example, the previous letter for b is a, the previous letter for s is r, the letter a has no previous letters. Note that after each removal the length of the string decreases by one. So, the index $$$i$$$ should satisfy the condition $$$1 \\le i \\le |s|$$$ during each operation.For the character $$$s_i$$$ adjacent characters are $$$s_{i-1}$$$ and $$$s_{i+1}$$$. The first and the last characters of $$$s$$$ both have only one adjacent character (unless $$$|s| = 1$$$).Consider the following example. Let $$$s=$$$ bacabcab.  During the first move, you can remove the first character $$$s_1=$$$ b because $$$s_2=$$$ a. Then the string becomes $$$s=$$$ acabcab.  During the second move, you can remove the fifth character $$$s_5=$$$ c because $$$s_4=$$$ b. Then the string becomes $$$s=$$$ acabab.  During the third move, you can remove the sixth character $$$s_6=$$$'b' because $$$s_5=$$$ a. Then the string becomes $$$s=$$$ acaba.  During the fourth move, the only character you can remove is $$$s_4=$$$ b, because $$$s_3=$$$ a (or $$$s_5=$$$ a). The string becomes $$$s=$$$ acaa and you cannot do anything with it. Your task is to find the maximum possible number of characters you can remove if you choose the sequence of operations optimally.",
  "input_from": "standard input",
  "output_to": "standard output",
  "time_limit": "2 seconds",
  "memory_limit": "256 megabytes",
  "input_spec": "The only line of the input contains one integer $$$|s|$$$ ($$$1 \\le |s| \\le 100$$$) \u2014 the length of $$$s$$$. The second line of the input contains one string $$$s$$$ consisting of $$$|s|$$$ lowercase Latin letters.",
  "output_spec": "Print one integer \u2014 the maximum possible number of characters you can remove if you choose the sequence of moves optimally.",
  "notes": "NoteThe first example is described in the problem statement. Note that the sequence of moves provided in the statement is not the only, but it can be shown that the maximum possible answer to this test is $$$4$$$.In the second example, you can remove all but one character of $$$s$$$. The only possible answer follows.  During the first move, remove the third character $$$s_3=$$$ d, $$$s$$$ becomes bca.  During the second move, remove the second character $$$s_2=$$$ c, $$$s$$$ becomes ba.  And during the third move, remove the first character $$$s_1=$$$ b, $$$s$$$ becomes a. ",
  "sample_inputs": [
    "8\nbacabcab",
    "4\nbcda",
    "6\nabbbbb"
  ],
  "sample_outputs": [
    "4",
    "3",
    "5"
  ],
  "tags": [
    "brute force",
    "constructive algorithms",
    "strings",
    "greedy"
  ],
  "src_uid": "9ce37bc2d361f5bb8a0568fb479b8a38",
  "difficulty": 1600
}
```

## Key Definitions

1. `lang`: Runtime/Compiler version of the `source_code`.
2. `source_code`: A program.
3. `tags`: List of potential algorithmic techniques required to write the program.
4. `lang_cluster`: A generic programming language name the value of `lang` belongs to.
5. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved. Refer to [Structure of `problem_descriptions.jsonl`](./README.md#structure-of-problem_descriptionsjsonl)
6. `code_uid`: A unique ID for the sample. It is not important for model training. If you find any issue with the sample, you can report it to us mentioning the `code_uid`.
7. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  
8. `exec_outcome`: Execution outcome status. Follow [Section 4.1](https://arxiv.org/pdf/2303.03004.pdf) to know the potential list of outcomes. The `exec_outcome` flags in the training data comes from a pre-run environmeent. However, training data doesn't  includes unit-test to avoid potential hacks. We provide unit test for only dev and test data.   
9. `sample_inputs`: A sample input for the code that is expected to solve the problem described in `description`.
10. `sample_outputs`: The expected output for the `sample_input` that is expected to solve the problem described in `description`.

## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c program_synthesis | md5sum
```

Output should match, `dcd0cb286721d78a0d40bfa20712bc67`.


## Tree

3 directories, 113 files

```
.
├── test
│   └── prog_syn_test.jsonl
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
    └── prog_syn_val.jsonl
```
