# Code Compilation Task

To download the code_compilation data,

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "code_compilation/*"
git lfs pull --include "problem_descriptions.jsonl"
```

Note that `code_compilation` data is extremely large. Feel free to download a subset of data first. 


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
6. `src_uid`: A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved. Refer to [Structure of `problem_descriptions.jsonl`](./README.md#structure-of-problem_descriptionsjsonl)
7. `difficulty`: Difficulty rating of the problem indicated by `src_uid`. The higher the harder.  


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c code_compilation | md5sum
```

Output should match, `24854d10e95089b79fca207053b5f1ae`.


# Tree

3 directories, 421 files

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
│   ├── train_0000.jsonl
│   ├── train_0001.jsonl
│   ├── train_0002.jsonl
│   ├── train_0003.jsonl
│   ├── train_0004.jsonl
│   ├── train_0005.jsonl
│   ├── train_0006.jsonl
│   ├── train_0007.jsonl
│   ├── train_0008.jsonl
│   ├── train_0009.jsonl
│   ├── train_0010.jsonl
│   ├── train_0011.jsonl
│   ├── train_0012.jsonl
│   ├── train_0013.jsonl
│   ├── train_0014.jsonl
│   ├── train_0015.jsonl
│   ├── train_0016.jsonl
│   ├── train_0017.jsonl
│   ├── train_0018.jsonl
│   ├── train_0019.jsonl
│   ├── train_0020.jsonl
│   ├── train_0021.jsonl
│   ├── train_0022.jsonl
│   ├── train_0023.jsonl
│   ├── train_0024.jsonl
│   ├── train_0025.jsonl
│   ├── train_0026.jsonl
│   ├── train_0027.jsonl
│   ├── train_0028.jsonl
│   ├── train_0029.jsonl
│   ├── train_0030.jsonl
│   ├── train_0031.jsonl
│   ├── train_0032.jsonl
│   ├── train_0033.jsonl
│   ├── train_0034.jsonl
│   ├── train_0035.jsonl
│   ├── train_0036.jsonl
│   ├── train_0037.jsonl
│   ├── train_0038.jsonl
│   ├── train_0039.jsonl
│   ├── train_0040.jsonl
│   ├── train_0041.jsonl
│   ├── train_0042.jsonl
│   ├── train_0043.jsonl
│   ├── train_0044.jsonl
│   ├── train_0045.jsonl
│   ├── train_0046.jsonl
│   ├── train_0047.jsonl
│   ├── train_0048.jsonl
│   ├── train_0049.jsonl
│   ├── train_0050.jsonl
│   ├── train_0051.jsonl
│   ├── train_0052.jsonl
│   ├── train_0053.jsonl
│   ├── train_0054.jsonl
│   ├── train_0055.jsonl
│   ├── train_0056.jsonl
│   ├── train_0057.jsonl
│   ├── train_0058.jsonl
│   ├── train_0059.jsonl
│   ├── train_0060.jsonl
│   ├── train_0061.jsonl
│   ├── train_0062.jsonl
│   ├── train_0063.jsonl
│   ├── train_0064.jsonl
│   ├── train_0065.jsonl
│   ├── train_0066.jsonl
│   ├── train_0067.jsonl
│   ├── train_0068.jsonl
│   ├── train_0069.jsonl
│   ├── train_0070.jsonl
│   ├── train_0071.jsonl
│   ├── train_0072.jsonl
│   ├── train_0073.jsonl
│   ├── train_0074.jsonl
│   ├── train_0075.jsonl
│   ├── train_0076.jsonl
│   ├── train_0077.jsonl
│   ├── train_0078.jsonl
│   ├── train_0079.jsonl
│   ├── train_0080.jsonl
│   ├── train_0081.jsonl
│   ├── train_0082.jsonl
│   ├── train_0083.jsonl
│   ├── train_0084.jsonl
│   ├── train_0085.jsonl
│   ├── train_0086.jsonl
│   ├── train_0087.jsonl
│   ├── train_0088.jsonl
│   ├── train_0089.jsonl
│   ├── train_0090.jsonl
│   ├── train_0091.jsonl
│   ├── train_0092.jsonl
│   ├── train_0093.jsonl
│   ├── train_0094.jsonl
│   ├── train_0095.jsonl
│   ├── train_0096.jsonl
│   ├── train_0097.jsonl
│   ├── train_0098.jsonl
│   ├── train_0099.jsonl
│   ├── train_0100.jsonl
│   ├── train_0101.jsonl
│   ├── train_0102.jsonl
│   ├── train_0103.jsonl
│   ├── train_0104.jsonl
│   ├── train_0105.jsonl
│   ├── train_0106.jsonl
│   ├── train_0107.jsonl
│   ├── train_0108.jsonl
│   ├── train_0109.jsonl
│   ├── train_0110.jsonl
│   ├── train_0111.jsonl
│   ├── train_0112.jsonl
│   ├── train_0113.jsonl
│   ├── train_0114.jsonl
│   ├── train_0115.jsonl
│   ├── train_0116.jsonl
│   ├── train_0117.jsonl
│   ├── train_0118.jsonl
│   ├── train_0119.jsonl
│   ├── train_0120.jsonl
│   ├── train_0121.jsonl
│   ├── train_0122.jsonl
│   ├── train_0123.jsonl
│   ├── train_0124.jsonl
│   ├── train_0125.jsonl
│   ├── train_0126.jsonl
│   ├── train_0127.jsonl
│   ├── train_0128.jsonl
│   ├── train_0129.jsonl
│   ├── train_0130.jsonl
│   ├── train_0131.jsonl
│   ├── train_0132.jsonl
│   ├── train_0133.jsonl
│   ├── train_0134.jsonl
│   ├── train_0135.jsonl
│   ├── train_0136.jsonl
│   ├── train_0137.jsonl
│   ├── train_0138.jsonl
│   ├── train_0139.jsonl
│   ├── train_0140.jsonl
│   ├── train_0141.jsonl
│   ├── train_0142.jsonl
│   ├── train_0143.jsonl
│   ├── train_0144.jsonl
│   ├── train_0145.jsonl
│   ├── train_0146.jsonl
│   ├── train_0147.jsonl
│   ├── train_0148.jsonl
│   ├── train_0149.jsonl
│   ├── train_0150.jsonl
│   ├── train_0151.jsonl
│   ├── train_0152.jsonl
│   ├── train_0153.jsonl
│   ├── train_0154.jsonl
│   ├── train_0155.jsonl
│   ├── train_0156.jsonl
│   ├── train_0157.jsonl
│   ├── train_0158.jsonl
│   ├── train_0159.jsonl
│   ├── train_0160.jsonl
│   ├── train_0161.jsonl
│   ├── train_0162.jsonl
│   ├── train_0163.jsonl
│   ├── train_0164.jsonl
│   ├── train_0165.jsonl
│   ├── train_0166.jsonl
│   ├── train_0167.jsonl
│   ├── train_0168.jsonl
│   ├── train_0169.jsonl
│   ├── train_0170.jsonl
│   ├── train_0171.jsonl
│   ├── train_0172.jsonl
│   ├── train_0173.jsonl
│   ├── train_0174.jsonl
│   ├── train_0175.jsonl
│   ├── train_0176.jsonl
│   ├── train_0177.jsonl
│   ├── train_0178.jsonl
│   ├── train_0179.jsonl
│   ├── train_0180.jsonl
│   ├── train_0181.jsonl
│   ├── train_0182.jsonl
│   ├── train_0183.jsonl
│   ├── train_0184.jsonl
│   ├── train_0185.jsonl
│   ├── train_0186.jsonl
│   ├── train_0187.jsonl
│   ├── train_0188.jsonl
│   ├── train_0189.jsonl
│   ├── train_0190.jsonl
│   ├── train_0191.jsonl
│   ├── train_0192.jsonl
│   ├── train_0193.jsonl
│   ├── train_0194.jsonl
│   ├── train_0195.jsonl
│   ├── train_0196.jsonl
│   ├── train_0197.jsonl
│   ├── train_0198.jsonl
│   ├── train_0199.jsonl
│   ├── train_0200.jsonl
│   ├── train_0201.jsonl
│   ├── train_0202.jsonl
│   ├── train_0203.jsonl
│   ├── train_0204.jsonl
│   ├── train_0205.jsonl
│   ├── train_0206.jsonl
│   ├── train_0207.jsonl
│   ├── train_0208.jsonl
│   ├── train_0209.jsonl
│   ├── train_0210.jsonl
│   ├── train_0211.jsonl
│   ├── train_0212.jsonl
│   ├── train_0213.jsonl
│   ├── train_0214.jsonl
│   ├── train_0215.jsonl
│   ├── train_0216.jsonl
│   ├── train_0217.jsonl
│   ├── train_0218.jsonl
│   ├── train_0219.jsonl
│   ├── train_0220.jsonl
│   ├── train_0221.jsonl
│   ├── train_0222.jsonl
│   ├── train_0223.jsonl
│   ├── train_0224.jsonl
│   ├── train_0225.jsonl
│   ├── train_0226.jsonl
│   ├── train_0227.jsonl
│   ├── train_0228.jsonl
│   ├── train_0229.jsonl
│   ├── train_0230.jsonl
│   ├── train_0231.jsonl
│   ├── train_0232.jsonl
│   ├── train_0233.jsonl
│   ├── train_0234.jsonl
│   ├── train_0235.jsonl
│   ├── train_0236.jsonl
│   ├── train_0237.jsonl
│   ├── train_0238.jsonl
│   ├── train_0239.jsonl
│   ├── train_0240.jsonl
│   ├── train_0241.jsonl
│   ├── train_0242.jsonl
│   ├── train_0243.jsonl
│   ├── train_0244.jsonl
│   ├── train_0245.jsonl
│   ├── train_0246.jsonl
│   ├── train_0247.jsonl
│   ├── train_0248.jsonl
│   ├── train_0249.jsonl
│   ├── train_0250.jsonl
│   ├── train_0251.jsonl
│   ├── train_0252.jsonl
│   ├── train_0253.jsonl
│   ├── train_0254.jsonl
│   ├── train_0255.jsonl
│   ├── train_0256.jsonl
│   ├── train_0257.jsonl
│   ├── train_0258.jsonl
│   ├── train_0259.jsonl
│   ├── train_0260.jsonl
│   ├── train_0261.jsonl
│   ├── train_0262.jsonl
│   ├── train_0263.jsonl
│   ├── train_0264.jsonl
│   ├── train_0265.jsonl
│   ├── train_0266.jsonl
│   ├── train_0267.jsonl
│   ├── train_0268.jsonl
│   ├── train_0269.jsonl
│   ├── train_0270.jsonl
│   ├── train_0271.jsonl
│   ├── train_0272.jsonl
│   ├── train_0273.jsonl
│   ├── train_0274.jsonl
│   ├── train_0275.jsonl
│   ├── train_0276.jsonl
│   ├── train_0277.jsonl
│   ├── train_0278.jsonl
│   ├── train_0279.jsonl
│   ├── train_0280.jsonl
│   ├── train_0281.jsonl
│   ├── train_0282.jsonl
│   ├── train_0283.jsonl
│   ├── train_0284.jsonl
│   ├── train_0285.jsonl
│   ├── train_0286.jsonl
│   ├── train_0287.jsonl
│   ├── train_0288.jsonl
│   ├── train_0289.jsonl
│   ├── train_0290.jsonl
│   ├── train_0291.jsonl
│   ├── train_0292.jsonl
│   ├── train_0293.jsonl
│   ├── train_0294.jsonl
│   ├── train_0295.jsonl
│   ├── train_0296.jsonl
│   ├── train_0297.jsonl
│   ├── train_0298.jsonl
│   ├── train_0299.jsonl
│   ├── train_0300.jsonl
│   ├── train_0301.jsonl
│   ├── train_0302.jsonl
│   ├── train_0303.jsonl
│   ├── train_0304.jsonl
│   ├── train_0305.jsonl
│   ├── train_0306.jsonl
│   ├── train_0307.jsonl
│   ├── train_0308.jsonl
│   ├── train_0309.jsonl
│   ├── train_0310.jsonl
│   ├── train_0311.jsonl
│   ├── train_0312.jsonl
│   ├── train_0313.jsonl
│   ├── train_0314.jsonl
│   ├── train_0315.jsonl
│   ├── train_0316.jsonl
│   ├── train_0317.jsonl
│   ├── train_0318.jsonl
│   ├── train_0319.jsonl
│   ├── train_0320.jsonl
│   ├── train_0321.jsonl
│   ├── train_0322.jsonl
│   ├── train_0323.jsonl
│   ├── train_0324.jsonl
│   ├── train_0325.jsonl
│   ├── train_0326.jsonl
│   ├── train_0327.jsonl
│   ├── train_0328.jsonl
│   ├── train_0329.jsonl
│   ├── train_0330.jsonl
│   ├── train_0331.jsonl
│   ├── train_0332.jsonl
│   ├── train_0333.jsonl
│   ├── train_0334.jsonl
│   ├── train_0335.jsonl
│   ├── train_0336.jsonl
│   ├── train_0337.jsonl
│   ├── train_0338.jsonl
│   ├── train_0339.jsonl
│   ├── train_0340.jsonl
│   ├── train_0341.jsonl
│   ├── train_0342.jsonl
│   ├── train_0343.jsonl
│   ├── train_0344.jsonl
│   ├── train_0345.jsonl
│   ├── train_0346.jsonl
│   ├── train_0347.jsonl
│   ├── train_0348.jsonl
│   ├── train_0349.jsonl
│   ├── train_0350.jsonl
│   ├── train_0351.jsonl
│   ├── train_0352.jsonl
│   ├── train_0353.jsonl
│   ├── train_0354.jsonl
│   ├── train_0355.jsonl
│   ├── train_0356.jsonl
│   ├── train_0357.jsonl
│   ├── train_0358.jsonl
│   ├── train_0359.jsonl
│   ├── train_0360.jsonl
│   ├── train_0361.jsonl
│   ├── train_0362.jsonl
│   ├── train_0363.jsonl
│   ├── train_0364.jsonl
│   ├── train_0365.jsonl
│   ├── train_0366.jsonl
│   ├── train_0367.jsonl
│   ├── train_0368.jsonl
│   ├── train_0369.jsonl
│   ├── train_0370.jsonl
│   ├── train_0371.jsonl
│   ├── train_0372.jsonl
│   ├── train_0373.jsonl
│   ├── train_0374.jsonl
│   ├── train_0375.jsonl
│   ├── train_0376.jsonl
│   ├── train_0377.jsonl
│   ├── train_0378.jsonl
│   ├── train_0379.jsonl
│   ├── train_0380.jsonl
│   ├── train_0381.jsonl
│   ├── train_0382.jsonl
│   ├── train_0383.jsonl
│   ├── train_0384.jsonl
│   ├── train_0385.jsonl
│   ├── train_0386.jsonl
│   ├── train_0387.jsonl
│   ├── train_0388.jsonl
│   ├── train_0389.jsonl
│   ├── train_0390.jsonl
│   ├── train_0391.jsonl
│   ├── train_0392.jsonl
│   ├── train_0393.jsonl
│   ├── train_0394.jsonl
│   ├── train_0395.jsonl
│   ├── train_0396.jsonl
│   ├── train_0397.jsonl
│   └── train_0398.jsonl
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
