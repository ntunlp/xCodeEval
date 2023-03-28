# Automatic Program Repair Task

## Tree

```
program_synthesis/
├── test
│   └── prog_syn_test.jsonl
├── train.jsonl
└── validation
    └── prog_syn_val.jsonl
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


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c apr | md5sum
```

Output should match, `fd0dec87dfffe5762f5e0af98a41ee32`.