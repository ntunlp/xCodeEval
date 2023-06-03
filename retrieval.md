# Code Retrieval

## Download data using huggingface `load_dataset()`

```
>>> import datasets
>>> retrieval_code_code_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "retrieval_code_code")
>>> print(retrieval_code_code_dataset)

DatasetDict({
    train: Dataset({
        features: ['negative_code', 'positive_code', 'source_code', 'file_name', 'src_uid'],
        num_rows: 50706
    })
    validation: Dataset({
        features: ['negative_code', 'positive_code', 'source_code', 'file_name', 'src_uid'],
        num_rows: 2535
    })
    test: Dataset({
        features: ['negative_code', 'positive_code', 'source_code', 'file_name', 'src_uid'],
        num_rows: 10044
    })
})

>>> retrieval_nl_code_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "retrieval_nl_code")
>>> print(retrieval_nl_code_dataset)

DatasetDict({
    train: Dataset({
        features: ['positive_code', 'negative_code', 'file_name', 'nl', 'src_uid'],
        num_rows: 61898
    })
    validation: Dataset({
        features: ['positive_code', 'negative_code', 'file_name', 'nl', 'src_uid'],
        num_rows: 2900
    })
    test: Dataset({
        features: ['positive_code', 'negative_code', 'file_name', 'nl', 'src_uid'],
        num_rows: 11701
    })
})

>>> retrieval_corpus_code_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "retrieval_corpus")
>>> print(retrieval_corpus_code_dataset)

DatasetDict({
    test: Dataset({
        features: ['file_name', 'source_code', 'idx'],
        num_rows: 25043700
    })
})
```


To download the retrieval data,

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull --include "retrieval_corpus/*"
git lfs pull --include "retrieval_nl_code/*"
git lfs pull --include "retrieval_code_code/*"
```

## A Sample from retrieval_corpus
```
{
	"idx": "9336887", 
	"source_code": "#include<iostream>\n#include<cmath>\n#include<cstdio>\n#include<cstring>\nusing namespace std;\nint main()\n{\n    long long n,a,b,c,cnt=0;\n    cin>>n>>a>>b>>c;\n    if(b-c>=a) cnt=n/a;\n    else\n    {\n        if(a>=b)\n        {\n            if(b>n)\n            {\n                cout<<0<<endl;\n                return 0;\n            }\n            n=n-b;\n            cnt=n/(b-c);\n            cnt=cnt+1;\n        }\n        else\n        {\n            if(a>n)\n            {\n                cout<<0<<endl;\n                return 0;\n            }\n            else if(a<=n&&b>n) cnt=n/a;\n            else\n            {\n                n=n-a;\n                cnt=n/(b-c);\n                ++cnt;\n            }\n        }\n    }\n    cout<<cnt<<endl;\n    return 0;\n}\n"}
```

## A sample from Train/Validation/Test split

A Sample from retrieval_nl_code,

```
{
	'nl': 
	'positive_code': [ ... , ... , ... , ... ]
	'negative_code', [ ... , ... , ... , ... ]
	'src_uid': 
}
```

A Sample from retrieval_code_code,

```
{
	'source_code': 
	'positive_code': [ ... , ... , ... , ... ]
	'negative_code', [ ... , ... , ... , ... ]
	'src_uid': 
}
```


## Key Definitions

1. `nl` : Problem description in textual format, math operations are written in latex. Given as input query.
2. `positive_code` : list of positive codes for `nl`
3. `negative_code` : list of negative codes for `nl`
4. `src_uid` : A specific identifier that shows which problem the code is associated with. This identifier is **important** for the training of the model. The problem referred to by the `src_uid` provides a natural description of the problem that the code successfully solved. Refer to [Structure of `problem_descriptions.jsonl`](./README.md#structure-of-problem_descriptionsjsonl)
5. `source_code` : A source code given as input query. 


## MD5 hash of the data

Run the following, 

```
cd xCodeEval/
tar c retrieval_corpus | md5sum
```

Output should match, `6d5f51cda332a65eb49e330484b8eb6f`.

```
cd xCodeEval/
tar c retrieval_nl_code | md5sum
```

Output should match, `cb8ca5339df596db1acebac5dd05f4b7`.

```
cd xCodeEval/
tar c retrieval_code_code | md5sum
```

Output should match, `3c4211ece767d513b8fa6b62e51fe962`.


## Tree

0 directories, 510 files

```
retrieval_corpus/
├── C#_code_retrieval_corpus.jsonl__000.jsonl
├── C++_code_retrieval_corpus.jsonl__000.jsonl
├── C_code_retrieval_corpus.jsonl__000.jsonl
├── C#_code_retrieval_corpus.jsonl__001.jsonl
├── C++_code_retrieval_corpus.jsonl__001.jsonl
├── C_code_retrieval_corpus.jsonl__001.jsonl
├── C#_code_retrieval_corpus.jsonl__002.jsonl
├── C++_code_retrieval_corpus.jsonl__002.jsonl
├── C_code_retrieval_corpus.jsonl__002.jsonl
├── C#_code_retrieval_corpus.jsonl__003.jsonl
├── C++_code_retrieval_corpus.jsonl__003.jsonl
├── C_code_retrieval_corpus.jsonl__003.jsonl
├── C#_code_retrieval_corpus.jsonl__004.jsonl
├── C++_code_retrieval_corpus.jsonl__004.jsonl
├── C_code_retrieval_corpus.jsonl__004.jsonl
├── C#_code_retrieval_corpus.jsonl__005.jsonl
├── C++_code_retrieval_corpus.jsonl__005.jsonl
├── C_code_retrieval_corpus.jsonl__005.jsonl
├── C++_code_retrieval_corpus.jsonl__006.jsonl
├── C_code_retrieval_corpus.jsonl__006.jsonl
├── C++_code_retrieval_corpus.jsonl__007.jsonl
├── C_code_retrieval_corpus.jsonl__007.jsonl
├── C++_code_retrieval_corpus.jsonl__008.jsonl
├── C_code_retrieval_corpus.jsonl__008.jsonl
├── C++_code_retrieval_corpus.jsonl__009.jsonl
├── C_code_retrieval_corpus.jsonl__009.jsonl
├── C++_code_retrieval_corpus.jsonl__010.jsonl
├── C_code_retrieval_corpus.jsonl__010.jsonl
├── C++_code_retrieval_corpus.jsonl__011.jsonl
├── C_code_retrieval_corpus.jsonl__011.jsonl
├── C++_code_retrieval_corpus.jsonl__012.jsonl
├── C_code_retrieval_corpus.jsonl__012.jsonl
├── C++_code_retrieval_corpus.jsonl__013.jsonl
├── C_code_retrieval_corpus.jsonl__013.jsonl
├── C++_code_retrieval_corpus.jsonl__014.jsonl
├── C_code_retrieval_corpus.jsonl__014.jsonl
├── C++_code_retrieval_corpus.jsonl__015.jsonl
├── C_code_retrieval_corpus.jsonl__015.jsonl
├── C++_code_retrieval_corpus.jsonl__016.jsonl
├── C++_code_retrieval_corpus.jsonl__017.jsonl
├── C++_code_retrieval_corpus.jsonl__018.jsonl
├── C++_code_retrieval_corpus.jsonl__019.jsonl
├── C++_code_retrieval_corpus.jsonl__020.jsonl
├── C++_code_retrieval_corpus.jsonl__021.jsonl
├── C++_code_retrieval_corpus.jsonl__022.jsonl
├── C++_code_retrieval_corpus.jsonl__023.jsonl
├── C++_code_retrieval_corpus.jsonl__024.jsonl
├── C++_code_retrieval_corpus.jsonl__025.jsonl
├── C++_code_retrieval_corpus.jsonl__026.jsonl
├── C++_code_retrieval_corpus.jsonl__027.jsonl
├── C++_code_retrieval_corpus.jsonl__028.jsonl
├── C++_code_retrieval_corpus.jsonl__029.jsonl
├── C++_code_retrieval_corpus.jsonl__030.jsonl
├── C++_code_retrieval_corpus.jsonl__031.jsonl
├── C++_code_retrieval_corpus.jsonl__032.jsonl
├── C++_code_retrieval_corpus.jsonl__033.jsonl
├── C++_code_retrieval_corpus.jsonl__034.jsonl
├── C++_code_retrieval_corpus.jsonl__035.jsonl
├── C++_code_retrieval_corpus.jsonl__036.jsonl
├── C++_code_retrieval_corpus.jsonl__037.jsonl
├── C++_code_retrieval_corpus.jsonl__038.jsonl
├── C++_code_retrieval_corpus.jsonl__039.jsonl
├── C++_code_retrieval_corpus.jsonl__040.jsonl
├── C++_code_retrieval_corpus.jsonl__041.jsonl
├── C++_code_retrieval_corpus.jsonl__042.jsonl
├── C++_code_retrieval_corpus.jsonl__043.jsonl
├── C++_code_retrieval_corpus.jsonl__044.jsonl
├── C++_code_retrieval_corpus.jsonl__045.jsonl
├── C++_code_retrieval_corpus.jsonl__046.jsonl
├── C++_code_retrieval_corpus.jsonl__047.jsonl
├── C++_code_retrieval_corpus.jsonl__048.jsonl
├── C++_code_retrieval_corpus.jsonl__049.jsonl
├── C++_code_retrieval_corpus.jsonl__050.jsonl
├── C++_code_retrieval_corpus.jsonl__051.jsonl
├── C++_code_retrieval_corpus.jsonl__052.jsonl
├── C++_code_retrieval_corpus.jsonl__053.jsonl
├── C++_code_retrieval_corpus.jsonl__054.jsonl
├── C++_code_retrieval_corpus.jsonl__055.jsonl
├── C++_code_retrieval_corpus.jsonl__056.jsonl
├── C++_code_retrieval_corpus.jsonl__057.jsonl
├── C++_code_retrieval_corpus.jsonl__058.jsonl
├── C++_code_retrieval_corpus.jsonl__059.jsonl
├── C++_code_retrieval_corpus.jsonl__060.jsonl
├── C++_code_retrieval_corpus.jsonl__061.jsonl
├── C++_code_retrieval_corpus.jsonl__062.jsonl
├── C++_code_retrieval_corpus.jsonl__063.jsonl
├── C++_code_retrieval_corpus.jsonl__064.jsonl
├── C++_code_retrieval_corpus.jsonl__065.jsonl
├── C++_code_retrieval_corpus.jsonl__066.jsonl
├── C++_code_retrieval_corpus.jsonl__067.jsonl
├── C++_code_retrieval_corpus.jsonl__068.jsonl
├── C++_code_retrieval_corpus.jsonl__069.jsonl
├── C++_code_retrieval_corpus.jsonl__070.jsonl
├── C++_code_retrieval_corpus.jsonl__071.jsonl
├── C++_code_retrieval_corpus.jsonl__072.jsonl
├── C++_code_retrieval_corpus.jsonl__073.jsonl
├── C++_code_retrieval_corpus.jsonl__074.jsonl
├── C++_code_retrieval_corpus.jsonl__075.jsonl
├── C++_code_retrieval_corpus.jsonl__076.jsonl
├── C++_code_retrieval_corpus.jsonl__077.jsonl
├── C++_code_retrieval_corpus.jsonl__078.jsonl
├── C++_code_retrieval_corpus.jsonl__079.jsonl
├── C++_code_retrieval_corpus.jsonl__080.jsonl
├── C++_code_retrieval_corpus.jsonl__081.jsonl
├── C++_code_retrieval_corpus.jsonl__082.jsonl
├── C++_code_retrieval_corpus.jsonl__083.jsonl
├── C++_code_retrieval_corpus.jsonl__084.jsonl
├── C++_code_retrieval_corpus.jsonl__085.jsonl
├── C++_code_retrieval_corpus.jsonl__086.jsonl
├── C++_code_retrieval_corpus.jsonl__087.jsonl
├── C++_code_retrieval_corpus.jsonl__088.jsonl
├── C++_code_retrieval_corpus.jsonl__089.jsonl
├── C++_code_retrieval_corpus.jsonl__090.jsonl
├── C++_code_retrieval_corpus.jsonl__091.jsonl
├── C++_code_retrieval_corpus.jsonl__092.jsonl
├── C++_code_retrieval_corpus.jsonl__093.jsonl
├── C++_code_retrieval_corpus.jsonl__094.jsonl
├── C++_code_retrieval_corpus.jsonl__095.jsonl
├── C++_code_retrieval_corpus.jsonl__096.jsonl
├── C++_code_retrieval_corpus.jsonl__097.jsonl
├── C++_code_retrieval_corpus.jsonl__098.jsonl
├── C++_code_retrieval_corpus.jsonl__099.jsonl
├── C++_code_retrieval_corpus.jsonl__100.jsonl
├── C++_code_retrieval_corpus.jsonl__101.jsonl
├── C++_code_retrieval_corpus.jsonl__102.jsonl
├── C++_code_retrieval_corpus.jsonl__103.jsonl
├── C++_code_retrieval_corpus.jsonl__104.jsonl
├── C++_code_retrieval_corpus.jsonl__105.jsonl
├── C++_code_retrieval_corpus.jsonl__106.jsonl
├── C++_code_retrieval_corpus.jsonl__107.jsonl
├── C++_code_retrieval_corpus.jsonl__108.jsonl
├── C++_code_retrieval_corpus.jsonl__109.jsonl
├── C++_code_retrieval_corpus.jsonl__110.jsonl
├── C++_code_retrieval_corpus.jsonl__111.jsonl
├── C++_code_retrieval_corpus.jsonl__112.jsonl
├── C++_code_retrieval_corpus.jsonl__113.jsonl
├── C++_code_retrieval_corpus.jsonl__114.jsonl
├── C++_code_retrieval_corpus.jsonl__115.jsonl
├── C++_code_retrieval_corpus.jsonl__116.jsonl
├── C++_code_retrieval_corpus.jsonl__117.jsonl
├── C++_code_retrieval_corpus.jsonl__118.jsonl
├── C++_code_retrieval_corpus.jsonl__119.jsonl
├── C++_code_retrieval_corpus.jsonl__120.jsonl
├── C++_code_retrieval_corpus.jsonl__121.jsonl
├── C++_code_retrieval_corpus.jsonl__122.jsonl
├── C++_code_retrieval_corpus.jsonl__123.jsonl
├── C++_code_retrieval_corpus.jsonl__124.jsonl
├── C++_code_retrieval_corpus.jsonl__125.jsonl
├── C++_code_retrieval_corpus.jsonl__126.jsonl
├── C++_code_retrieval_corpus.jsonl__127.jsonl
├── C++_code_retrieval_corpus.jsonl__128.jsonl
├── C++_code_retrieval_corpus.jsonl__129.jsonl
├── C++_code_retrieval_corpus.jsonl__130.jsonl
├── C++_code_retrieval_corpus.jsonl__131.jsonl
├── C++_code_retrieval_corpus.jsonl__132.jsonl
├── C++_code_retrieval_corpus.jsonl__133.jsonl
├── C++_code_retrieval_corpus.jsonl__134.jsonl
├── C++_code_retrieval_corpus.jsonl__135.jsonl
├── C++_code_retrieval_corpus.jsonl__136.jsonl
├── C++_code_retrieval_corpus.jsonl__137.jsonl
├── C++_code_retrieval_corpus.jsonl__138.jsonl
├── C++_code_retrieval_corpus.jsonl__139.jsonl
├── C++_code_retrieval_corpus.jsonl__140.jsonl
├── C++_code_retrieval_corpus.jsonl__141.jsonl
├── C++_code_retrieval_corpus.jsonl__142.jsonl
├── C++_code_retrieval_corpus.jsonl__143.jsonl
├── C++_code_retrieval_corpus.jsonl__144.jsonl
├── C++_code_retrieval_corpus.jsonl__145.jsonl
├── C++_code_retrieval_corpus.jsonl__146.jsonl
├── C++_code_retrieval_corpus.jsonl__147.jsonl
├── C++_code_retrieval_corpus.jsonl__148.jsonl
├── C++_code_retrieval_corpus.jsonl__149.jsonl
├── C++_code_retrieval_corpus.jsonl__150.jsonl
├── C++_code_retrieval_corpus.jsonl__151.jsonl
├── C++_code_retrieval_corpus.jsonl__152.jsonl
├── C++_code_retrieval_corpus.jsonl__153.jsonl
├── C++_code_retrieval_corpus.jsonl__154.jsonl
├── C++_code_retrieval_corpus.jsonl__155.jsonl
├── C++_code_retrieval_corpus.jsonl__156.jsonl
├── C++_code_retrieval_corpus.jsonl__157.jsonl
├── C++_code_retrieval_corpus.jsonl__158.jsonl
├── C++_code_retrieval_corpus.jsonl__159.jsonl
├── C++_code_retrieval_corpus.jsonl__160.jsonl
├── C++_code_retrieval_corpus.jsonl__161.jsonl
├── C++_code_retrieval_corpus.jsonl__162.jsonl
├── C++_code_retrieval_corpus.jsonl__163.jsonl
├── C++_code_retrieval_corpus.jsonl__164.jsonl
├── C++_code_retrieval_corpus.jsonl__165.jsonl
├── C++_code_retrieval_corpus.jsonl__166.jsonl
├── C++_code_retrieval_corpus.jsonl__167.jsonl
├── C++_code_retrieval_corpus.jsonl__168.jsonl
├── C++_code_retrieval_corpus.jsonl__169.jsonl
├── C++_code_retrieval_corpus.jsonl__170.jsonl
├── C++_code_retrieval_corpus.jsonl__171.jsonl
├── C++_code_retrieval_corpus.jsonl__172.jsonl
├── C++_code_retrieval_corpus.jsonl__173.jsonl
├── C++_code_retrieval_corpus.jsonl__174.jsonl
├── C++_code_retrieval_corpus.jsonl__175.jsonl
├── C++_code_retrieval_corpus.jsonl__176.jsonl
├── C++_code_retrieval_corpus.jsonl__177.jsonl
├── C++_code_retrieval_corpus.jsonl__178.jsonl
├── C++_code_retrieval_corpus.jsonl__179.jsonl
├── C++_code_retrieval_corpus.jsonl__180.jsonl
├── C++_code_retrieval_corpus.jsonl__181.jsonl
├── C++_code_retrieval_corpus.jsonl__182.jsonl
├── C++_code_retrieval_corpus.jsonl__183.jsonl
├── C++_code_retrieval_corpus.jsonl__184.jsonl
├── C++_code_retrieval_corpus.jsonl__185.jsonl
├── C++_code_retrieval_corpus.jsonl__186.jsonl
├── C++_code_retrieval_corpus.jsonl__187.jsonl
├── C++_code_retrieval_corpus.jsonl__188.jsonl
├── C++_code_retrieval_corpus.jsonl__189.jsonl
├── C++_code_retrieval_corpus.jsonl__190.jsonl
├── C++_code_retrieval_corpus.jsonl__191.jsonl
├── C++_code_retrieval_corpus.jsonl__192.jsonl
├── C++_code_retrieval_corpus.jsonl__193.jsonl
├── C++_code_retrieval_corpus.jsonl__194.jsonl
├── C++_code_retrieval_corpus.jsonl__195.jsonl
├── C++_code_retrieval_corpus.jsonl__196.jsonl
├── C++_code_retrieval_corpus.jsonl__197.jsonl
├── C++_code_retrieval_corpus.jsonl__198.jsonl
├── C++_code_retrieval_corpus.jsonl__199.jsonl
├── C++_code_retrieval_corpus.jsonl__200.jsonl
├── C++_code_retrieval_corpus.jsonl__201.jsonl
├── C++_code_retrieval_corpus.jsonl__202.jsonl
├── C++_code_retrieval_corpus.jsonl__203.jsonl
├── C++_code_retrieval_corpus.jsonl__204.jsonl
├── C++_code_retrieval_corpus.jsonl__205.jsonl
├── C++_code_retrieval_corpus.jsonl__206.jsonl
├── C++_code_retrieval_corpus.jsonl__207.jsonl
├── C++_code_retrieval_corpus.jsonl__208.jsonl
├── C++_code_retrieval_corpus.jsonl__209.jsonl
├── C++_code_retrieval_corpus.jsonl__210.jsonl
├── C++_code_retrieval_corpus.jsonl__211.jsonl
├── C++_code_retrieval_corpus.jsonl__212.jsonl
├── C++_code_retrieval_corpus.jsonl__213.jsonl
├── C++_code_retrieval_corpus.jsonl__214.jsonl
├── C++_code_retrieval_corpus.jsonl__215.jsonl
├── C++_code_retrieval_corpus.jsonl__216.jsonl
├── C++_code_retrieval_corpus.jsonl__217.jsonl
├── C++_code_retrieval_corpus.jsonl__218.jsonl
├── C++_code_retrieval_corpus.jsonl__219.jsonl
├── C++_code_retrieval_corpus.jsonl__220.jsonl
├── C++_code_retrieval_corpus.jsonl__221.jsonl
├── C++_code_retrieval_corpus.jsonl__222.jsonl
├── C++_code_retrieval_corpus.jsonl__223.jsonl
├── C++_code_retrieval_corpus.jsonl__224.jsonl
├── C++_code_retrieval_corpus.jsonl__225.jsonl
├── C++_code_retrieval_corpus.jsonl__226.jsonl
├── C++_code_retrieval_corpus.jsonl__227.jsonl
├── C++_code_retrieval_corpus.jsonl__228.jsonl
├── C++_code_retrieval_corpus.jsonl__229.jsonl
├── C++_code_retrieval_corpus.jsonl__230.jsonl
├── C++_code_retrieval_corpus.jsonl__231.jsonl
├── C++_code_retrieval_corpus.jsonl__232.jsonl
├── C++_code_retrieval_corpus.jsonl__233.jsonl
├── C++_code_retrieval_corpus.jsonl__234.jsonl
├── C++_code_retrieval_corpus.jsonl__235.jsonl
├── C++_code_retrieval_corpus.jsonl__236.jsonl
├── C++_code_retrieval_corpus.jsonl__237.jsonl
├── C++_code_retrieval_corpus.jsonl__238.jsonl
├── C++_code_retrieval_corpus.jsonl__239.jsonl
├── C++_code_retrieval_corpus.jsonl__240.jsonl
├── C++_code_retrieval_corpus.jsonl__241.jsonl
├── C++_code_retrieval_corpus.jsonl__242.jsonl
├── C++_code_retrieval_corpus.jsonl__243.jsonl
├── C++_code_retrieval_corpus.jsonl__244.jsonl
├── C++_code_retrieval_corpus.jsonl__245.jsonl
├── C++_code_retrieval_corpus.jsonl__246.jsonl
├── C++_code_retrieval_corpus.jsonl__247.jsonl
├── C++_code_retrieval_corpus.jsonl__248.jsonl
├── C++_code_retrieval_corpus.jsonl__249.jsonl
├── C++_code_retrieval_corpus.jsonl__250.jsonl
├── C++_code_retrieval_corpus.jsonl__251.jsonl
├── C++_code_retrieval_corpus.jsonl__252.jsonl
├── C++_code_retrieval_corpus.jsonl__253.jsonl
├── C++_code_retrieval_corpus.jsonl__254.jsonl
├── C++_code_retrieval_corpus.jsonl__255.jsonl
├── C++_code_retrieval_corpus.jsonl__256.jsonl
├── C++_code_retrieval_corpus.jsonl__257.jsonl
├── C++_code_retrieval_corpus.jsonl__258.jsonl
├── C++_code_retrieval_corpus.jsonl__259.jsonl
├── C++_code_retrieval_corpus.jsonl__260.jsonl
├── C++_code_retrieval_corpus.jsonl__261.jsonl
├── C++_code_retrieval_corpus.jsonl__262.jsonl
├── C++_code_retrieval_corpus.jsonl__263.jsonl
├── C++_code_retrieval_corpus.jsonl__264.jsonl
├── C++_code_retrieval_corpus.jsonl__265.jsonl
├── C++_code_retrieval_corpus.jsonl__266.jsonl
├── C++_code_retrieval_corpus.jsonl__267.jsonl
├── C++_code_retrieval_corpus.jsonl__268.jsonl
├── C++_code_retrieval_corpus.jsonl__269.jsonl
├── C++_code_retrieval_corpus.jsonl__270.jsonl
├── C++_code_retrieval_corpus.jsonl__271.jsonl
├── C++_code_retrieval_corpus.jsonl__272.jsonl
├── C++_code_retrieval_corpus.jsonl__273.jsonl
├── C++_code_retrieval_corpus.jsonl__274.jsonl
├── C++_code_retrieval_corpus.jsonl__275.jsonl
├── C++_code_retrieval_corpus.jsonl__276.jsonl
├── C++_code_retrieval_corpus.jsonl__277.jsonl
├── C++_code_retrieval_corpus.jsonl__278.jsonl
├── C++_code_retrieval_corpus.jsonl__279.jsonl
├── C++_code_retrieval_corpus.jsonl__280.jsonl
├── C++_code_retrieval_corpus.jsonl__281.jsonl
├── C++_code_retrieval_corpus.jsonl__282.jsonl
├── C++_code_retrieval_corpus.jsonl__283.jsonl
├── C++_code_retrieval_corpus.jsonl__284.jsonl
├── C++_code_retrieval_corpus.jsonl__285.jsonl
├── C++_code_retrieval_corpus.jsonl__286.jsonl
├── C++_code_retrieval_corpus.jsonl__287.jsonl
├── C++_code_retrieval_corpus.jsonl__288.jsonl
├── C++_code_retrieval_corpus.jsonl__289.jsonl
├── C++_code_retrieval_corpus.jsonl__290.jsonl
├── C++_code_retrieval_corpus.jsonl__291.jsonl
├── C++_code_retrieval_corpus.jsonl__292.jsonl
├── C++_code_retrieval_corpus.jsonl__293.jsonl
├── C++_code_retrieval_corpus.jsonl__294.jsonl
├── C++_code_retrieval_corpus.jsonl__295.jsonl
├── C++_code_retrieval_corpus.jsonl__296.jsonl
├── C++_code_retrieval_corpus.jsonl__297.jsonl
├── C++_code_retrieval_corpus.jsonl__298.jsonl
├── C++_code_retrieval_corpus.jsonl__299.jsonl
├── C++_code_retrieval_corpus.jsonl__300.jsonl
├── C++_code_retrieval_corpus.jsonl__301.jsonl
├── C++_code_retrieval_corpus.jsonl__302.jsonl
├── C++_code_retrieval_corpus.jsonl__303.jsonl
├── C++_code_retrieval_corpus.jsonl__304.jsonl
├── C++_code_retrieval_corpus.jsonl__305.jsonl
├── C++_code_retrieval_corpus.jsonl__306.jsonl
├── C++_code_retrieval_corpus.jsonl__307.jsonl
├── C++_code_retrieval_corpus.jsonl__308.jsonl
├── C++_code_retrieval_corpus.jsonl__309.jsonl
├── C++_code_retrieval_corpus.jsonl__310.jsonl
├── C++_code_retrieval_corpus.jsonl__311.jsonl
├── C++_code_retrieval_corpus.jsonl__312.jsonl
├── C++_code_retrieval_corpus.jsonl__313.jsonl
├── C++_code_retrieval_corpus.jsonl__314.jsonl
├── C++_code_retrieval_corpus.jsonl__315.jsonl
├── C++_code_retrieval_corpus.jsonl__316.jsonl
├── C++_code_retrieval_corpus.jsonl__317.jsonl
├── C++_code_retrieval_corpus.jsonl__318.jsonl
├── C++_code_retrieval_corpus.jsonl__319.jsonl
├── C++_code_retrieval_corpus.jsonl__320.jsonl
├── C++_code_retrieval_corpus.jsonl__321.jsonl
├── C++_code_retrieval_corpus.jsonl__322.jsonl
├── C++_code_retrieval_corpus.jsonl__323.jsonl
├── C++_code_retrieval_corpus.jsonl__324.jsonl
├── C++_code_retrieval_corpus.jsonl__325.jsonl
├── C++_code_retrieval_corpus.jsonl__326.jsonl
├── C++_code_retrieval_corpus.jsonl__327.jsonl
├── C++_code_retrieval_corpus.jsonl__328.jsonl
├── C++_code_retrieval_corpus.jsonl__329.jsonl
├── C++_code_retrieval_corpus.jsonl__330.jsonl
├── C++_code_retrieval_corpus.jsonl__331.jsonl
├── C++_code_retrieval_corpus.jsonl__332.jsonl
├── C++_code_retrieval_corpus.jsonl__333.jsonl
├── C++_code_retrieval_corpus.jsonl__334.jsonl
├── C++_code_retrieval_corpus.jsonl__335.jsonl
├── C++_code_retrieval_corpus.jsonl__336.jsonl
├── C++_code_retrieval_corpus.jsonl__337.jsonl
├── C++_code_retrieval_corpus.jsonl__338.jsonl
├── C++_code_retrieval_corpus.jsonl__339.jsonl
├── C++_code_retrieval_corpus.jsonl__340.jsonl
├── C++_code_retrieval_corpus.jsonl__341.jsonl
├── C++_code_retrieval_corpus.jsonl__342.jsonl
├── C++_code_retrieval_corpus.jsonl__343.jsonl
├── C++_code_retrieval_corpus.jsonl__344.jsonl
├── C++_code_retrieval_corpus.jsonl__345.jsonl
├── C++_code_retrieval_corpus.jsonl__346.jsonl
├── C++_code_retrieval_corpus.jsonl__347.jsonl
├── C++_code_retrieval_corpus.jsonl__348.jsonl
├── C++_code_retrieval_corpus.jsonl__349.jsonl
├── C++_code_retrieval_corpus.jsonl__350.jsonl
├── C++_code_retrieval_corpus.jsonl__351.jsonl
├── C++_code_retrieval_corpus.jsonl__352.jsonl
├── C++_code_retrieval_corpus.jsonl__353.jsonl
├── C++_code_retrieval_corpus.jsonl__354.jsonl
├── C++_code_retrieval_corpus.jsonl__355.jsonl
├── C++_code_retrieval_corpus.jsonl__356.jsonl
├── C++_code_retrieval_corpus.jsonl__357.jsonl
├── C++_code_retrieval_corpus.jsonl__358.jsonl
├── C++_code_retrieval_corpus.jsonl__359.jsonl
├── C++_code_retrieval_corpus.jsonl__360.jsonl
├── C++_code_retrieval_corpus.jsonl__361.jsonl
├── C++_code_retrieval_corpus.jsonl__362.jsonl
├── C++_code_retrieval_corpus.jsonl__363.jsonl
├── C++_code_retrieval_corpus.jsonl__364.jsonl
├── D_code_retrieval_corpus.jsonl__000.jsonl
├── Go_code_retrieval_corpus.jsonl__000.jsonl
├── Go_code_retrieval_corpus.jsonl__001.jsonl
├── Haskell_code_retrieval_corpus.jsonl__000.jsonl
├── Java_code_retrieval_corpus.jsonl__000.jsonl
├── Java_code_retrieval_corpus.jsonl__001.jsonl
├── Java_code_retrieval_corpus.jsonl__002.jsonl
├── Java_code_retrieval_corpus.jsonl__003.jsonl
├── Java_code_retrieval_corpus.jsonl__004.jsonl
├── Java_code_retrieval_corpus.jsonl__005.jsonl
├── Java_code_retrieval_corpus.jsonl__006.jsonl
├── Java_code_retrieval_corpus.jsonl__007.jsonl
├── Java_code_retrieval_corpus.jsonl__008.jsonl
├── Java_code_retrieval_corpus.jsonl__009.jsonl
├── Java_code_retrieval_corpus.jsonl__010.jsonl
├── Java_code_retrieval_corpus.jsonl__011.jsonl
├── Java_code_retrieval_corpus.jsonl__012.jsonl
├── Java_code_retrieval_corpus.jsonl__013.jsonl
├── Java_code_retrieval_corpus.jsonl__014.jsonl
├── Java_code_retrieval_corpus.jsonl__015.jsonl
├── Java_code_retrieval_corpus.jsonl__016.jsonl
├── Java_code_retrieval_corpus.jsonl__017.jsonl
├── Java_code_retrieval_corpus.jsonl__018.jsonl
├── Java_code_retrieval_corpus.jsonl__019.jsonl
├── Java_code_retrieval_corpus.jsonl__020.jsonl
├── Java_code_retrieval_corpus.jsonl__021.jsonl
├── Java_code_retrieval_corpus.jsonl__022.jsonl
├── Java_code_retrieval_corpus.jsonl__023.jsonl
├── Java_code_retrieval_corpus.jsonl__024.jsonl
├── Java_code_retrieval_corpus.jsonl__025.jsonl
├── Java_code_retrieval_corpus.jsonl__026.jsonl
├── Java_code_retrieval_corpus.jsonl__027.jsonl
├── Java_code_retrieval_corpus.jsonl__028.jsonl
├── Java_code_retrieval_corpus.jsonl__029.jsonl
├── Java_code_retrieval_corpus.jsonl__030.jsonl
├── Java_code_retrieval_corpus.jsonl__031.jsonl
├── Java_code_retrieval_corpus.jsonl__032.jsonl
├── Java_code_retrieval_corpus.jsonl__033.jsonl
├── Java_code_retrieval_corpus.jsonl__034.jsonl
├── Java_code_retrieval_corpus.jsonl__035.jsonl
├── Java_code_retrieval_corpus.jsonl__036.jsonl
├── Java_code_retrieval_corpus.jsonl__037.jsonl
├── Java_code_retrieval_corpus.jsonl__038.jsonl
├── Java_code_retrieval_corpus.jsonl__039.jsonl
├── Java_code_retrieval_corpus.jsonl__040.jsonl
├── Java_code_retrieval_corpus.jsonl__041.jsonl
├── Java_code_retrieval_corpus.jsonl__042.jsonl
├── Java_code_retrieval_corpus.jsonl__043.jsonl
├── Java_code_retrieval_corpus.jsonl__044.jsonl
├── Java_code_retrieval_corpus.jsonl__045.jsonl
├── Java_code_retrieval_corpus.jsonl__046.jsonl
├── Java_code_retrieval_corpus.jsonl__047.jsonl
├── Java_code_retrieval_corpus.jsonl__048.jsonl
├── Java_code_retrieval_corpus.jsonl__049.jsonl
├── Java_code_retrieval_corpus.jsonl__050.jsonl
├── Javascript_code_retrieval_corpus.jsonl__000.jsonl
├── Javascript_code_retrieval_corpus.jsonl__001.jsonl
├── Kotlin_code_retrieval_corpus.jsonl__000.jsonl
├── Kotlin_code_retrieval_corpus.jsonl__001.jsonl
├── Kotlin_code_retrieval_corpus.jsonl__002.jsonl
├── Ocaml_code_retrieval_corpus.jsonl__000.jsonl
├── Pascal_code_retrieval_corpus.jsonl__000.jsonl
├── Pascal_code_retrieval_corpus.jsonl__001.jsonl
├── Pascal_code_retrieval_corpus.jsonl__002.jsonl
├── Pascal_code_retrieval_corpus.jsonl__003.jsonl
├── Pascal_code_retrieval_corpus.jsonl__004.jsonl
├── Pascal_code_retrieval_corpus.jsonl__005.jsonl
├── Pascal_code_retrieval_corpus.jsonl__006.jsonl
├── Pascal_code_retrieval_corpus.jsonl__007.jsonl
├── Pascal_code_retrieval_corpus.jsonl__008.jsonl
├── Pascal_code_retrieval_corpus.jsonl__009.jsonl
├── Perl_code_retrieval_corpus.jsonl__000.jsonl
├── PHP_code_retrieval_corpus.jsonl__000.jsonl
├── Python_code_retrieval_corpus.jsonl__000.jsonl
├── Python_code_retrieval_corpus.jsonl__001.jsonl
├── Python_code_retrieval_corpus.jsonl__002.jsonl
├── Python_code_retrieval_corpus.jsonl__003.jsonl
├── Python_code_retrieval_corpus.jsonl__004.jsonl
├── Python_code_retrieval_corpus.jsonl__005.jsonl
├── Python_code_retrieval_corpus.jsonl__006.jsonl
├── Python_code_retrieval_corpus.jsonl__007.jsonl
├── Python_code_retrieval_corpus.jsonl__008.jsonl
├── Python_code_retrieval_corpus.jsonl__009.jsonl
├── Python_code_retrieval_corpus.jsonl__010.jsonl
├── Python_code_retrieval_corpus.jsonl__011.jsonl
├── Python_code_retrieval_corpus.jsonl__012.jsonl
├── Python_code_retrieval_corpus.jsonl__013.jsonl
├── Python_code_retrieval_corpus.jsonl__014.jsonl
├── Python_code_retrieval_corpus.jsonl__015.jsonl
├── Python_code_retrieval_corpus.jsonl__016.jsonl
├── Python_code_retrieval_corpus.jsonl__017.jsonl
├── Python_code_retrieval_corpus.jsonl__018.jsonl
├── Python_code_retrieval_corpus.jsonl__019.jsonl
├── Python_code_retrieval_corpus.jsonl__020.jsonl
├── Python_code_retrieval_corpus.jsonl__021.jsonl
├── Python_code_retrieval_corpus.jsonl__022.jsonl
├── Python_code_retrieval_corpus.jsonl__023.jsonl
├── Python_code_retrieval_corpus.jsonl__024.jsonl
├── Python_code_retrieval_corpus.jsonl__025.jsonl
├── Python_code_retrieval_corpus.jsonl__026.jsonl
├── Python_code_retrieval_corpus.jsonl__027.jsonl
├── Python_code_retrieval_corpus.jsonl__028.jsonl
├── Python_code_retrieval_corpus.jsonl__029.jsonl
├── Python_code_retrieval_corpus.jsonl__030.jsonl
├── Python_code_retrieval_corpus.jsonl__031.jsonl
├── Python_code_retrieval_corpus.jsonl__032.jsonl
├── Python_code_retrieval_corpus.jsonl__033.jsonl
├── Python_code_retrieval_corpus.jsonl__034.jsonl
├── Python_code_retrieval_corpus.jsonl__035.jsonl
├── Python_code_retrieval_corpus.jsonl__036.jsonl
├── Python_code_retrieval_corpus.jsonl__037.jsonl
├── Python_code_retrieval_corpus.jsonl__038.jsonl
├── Python_code_retrieval_corpus.jsonl__039.jsonl
├── Python_code_retrieval_corpus.jsonl__040.jsonl
├── Python_code_retrieval_corpus.jsonl__041.jsonl
├── Python_code_retrieval_corpus.jsonl__042.jsonl
├── Python_code_retrieval_corpus.jsonl__043.jsonl
├── Python_code_retrieval_corpus.jsonl__044.jsonl
├── Python_code_retrieval_corpus.jsonl__045.jsonl
├── Ruby_code_retrieval_corpus.jsonl__000.jsonl
├── Rust_code_retrieval_corpus.jsonl__000.jsonl
├── Rust_code_retrieval_corpus.jsonl__001.jsonl
└── Scala_code_retrieval_corpus.jsonl__000.jsonl
```

3 directories, 62 files

```
retrieval_nl_code/
├── dev
│   ├── C#_nl_code_dev_file.jsonl
│   ├── C++_nl_code_dev_file.jsonl
│   ├── C_nl_code_dev_file.jsonl
│   ├── D_nl_code_dev_file.jsonl
│   ├── Go_nl_code_dev_file.jsonl
│   ├── Haskell_nl_code_dev_file.jsonl
│   ├── Java_nl_code_dev_file.jsonl
│   ├── Javascript_nl_code_dev_file.jsonl
│   ├── Kotlin_nl_code_dev_file.jsonl
│   ├── Ocaml_nl_code_dev_file.jsonl
│   ├── Pascal_nl_code_dev_file.jsonl
│   ├── Perl_nl_code_dev_file.jsonl
│   ├── PHP_nl_code_dev_file.jsonl
│   ├── Python_nl_code_dev_file.jsonl
│   ├── Ruby_nl_code_dev_file.jsonl
│   ├── Rust_nl_code_dev_file.jsonl
│   └── Scala_nl_code_dev_file.jsonl
├── test
│   ├── C#_nl_code_test_file.jsonl
│   ├── C++_nl_code_test_file.jsonl
│   ├── C_nl_code_test_file.jsonl
│   ├── D_nl_code_test_file.jsonl
│   ├── Go_nl_code_test_file.jsonl
│   ├── Haskell_nl_code_test_file.jsonl
│   ├── Java_nl_code_test_file.jsonl
│   ├── Javascript_nl_code_test_file.jsonl
│   ├── Kotlin_nl_code_test_file.jsonl
│   ├── Ocaml_nl_code_test_file.jsonl
│   ├── Pascal_nl_code_test_file.jsonl
│   ├── Perl_nl_code_test_file.jsonl
│   ├── PHP_nl_code_test_file.jsonl
│   ├── Python_nl_code_test_file.jsonl
│   ├── Ruby_nl_code_test_file.jsonl
│   ├── Rust_nl_code_test_file.jsonl
│   └── Scala_nl_code_test_file.jsonl
└── train
    ├── C++_nl_code_train_file_000.jsonl
    ├── C++_nl_code_train_file_001.jsonl
    ├── C++_nl_code_train_file_002.jsonl
    ├── C++_nl_code_train_file_003.jsonl
    ├── C++_nl_code_train_file_004.jsonl
    ├── C++_nl_code_train_file_005.jsonl
    ├── C++_nl_code_train_file_006.jsonl
    ├── C#_nl_code_train_file.jsonl
    ├── C_nl_code_train_file.jsonl
    ├── D_nl_code_train_file.jsonl
    ├── Go_nl_code_train_file.jsonl
    ├── Haskell_nl_code_train_file.jsonl
    ├── Java_nl_code_train_file_000.jsonl
    ├── Java_nl_code_train_file_001.jsonl
    ├── Java_nl_code_train_file_002.jsonl
    ├── Java_nl_code_train_file_003.jsonl
    ├── Java_nl_code_train_file_004.jsonl
    ├── Java_nl_code_train_file_005.jsonl
    ├── Javascript_nl_code_train_file.jsonl
    ├── Kotlin_nl_code_train_file.jsonl
    ├── Ocaml_nl_code_train_file.jsonl
    ├── Pascal_nl_code_train_file.jsonl
    ├── Perl_nl_code_train_file.jsonl
    ├── PHP_nl_code_train_file.jsonl
    ├── Python_nl_code_train_file.jsonl
    ├── Ruby_nl_code_train_file.jsonl
    ├── Rust_nl_code_train_file.jsonl
    └── Scala_nl_code_train_file.jsonl
```

3 directories, 62 files

```
retrieval_code_code/
├── dev
│   ├── C#_code_code_dev_file.jsonl
│   ├── C++_code_code_dev_file.jsonl
│   ├── C_code_code_dev_file.jsonl
│   ├── D_code_code_dev_file.jsonl
│   ├── Go_code_code_dev_file.jsonl
│   ├── Haskell_code_code_dev_file.jsonl
│   ├── Java_code_code_dev_file.jsonl
│   ├── Javascript_code_code_dev_file.jsonl
│   ├── Kotlin_code_code_dev_file.jsonl
│   ├── Ocaml_code_code_dev_file.jsonl
│   ├── Pascal_code_code_dev_file.jsonl
│   ├── Perl_code_code_dev_file.jsonl
│   ├── PHP_code_code_dev_file.jsonl
│   ├── Python_code_code_dev_file.jsonl
│   ├── Ruby_code_code_dev_file.jsonl
│   ├── Rust_code_code_dev_file.jsonl
│   └── Scala_code_code_dev_file.jsonl
├── test
│   ├── C#_code_code_test_file.jsonl
│   ├── C++_code_code_test_file.jsonl
│   ├── C_code_code_test_file.jsonl
│   ├── D_code_code_test_file.jsonl
│   ├── Go_code_code_test_file.jsonl
│   ├── Haskell_code_code_test_file.jsonl
│   ├── Java_code_code_test_file.jsonl
│   ├── Javascript_code_code_test_file.jsonl
│   ├── Kotlin_code_code_test_file.jsonl
│   ├── Ocaml_code_code_test_file.jsonl
│   ├── Pascal_code_code_test_file.jsonl
│   ├── Perl_code_code_test_file.jsonl
│   ├── PHP_code_code_test_file.jsonl
│   ├── Python_code_code_test_file.jsonl
│   ├── Ruby_code_code_test_file.jsonl
│   ├── Rust_code_code_test_file.jsonl
│   └── Scala_code_code_test_file.jsonl
└── train
    ├── C++_code_code_train_file_000.jsonl
    ├── C++_code_code_train_file_001.jsonl
    ├── C++_code_code_train_file_002.jsonl
    ├── C++_code_code_train_file_003.jsonl
    ├── C++_code_code_train_file_004.jsonl
    ├── C++_code_code_train_file_005.jsonl
    ├── C++_code_code_train_file_006.jsonl
    ├── C#_code_code_train_file.jsonl
    ├── C_code_code_train_file.jsonl
    ├── D_code_code_train_file.jsonl
    ├── Go_code_code_train_file.jsonl
    ├── Haskell_code_code_train_file.jsonl
    ├── Java_code_code_train_file_000.jsonl
    ├── Java_code_code_train_file_001.jsonl
    ├── Java_code_code_train_file_002.jsonl
    ├── Java_code_code_train_file_003.jsonl
    ├── Java_code_code_train_file_004.jsonl
    ├── Java_code_code_train_file_005.jsonl
    ├── Javascript_code_code_train_file.jsonl
    ├── Kotlin_code_code_train_file.jsonl
    ├── Ocaml_code_code_train_file.jsonl
    ├── Pascal_code_code_train_file.jsonl
    ├── Perl_code_code_train_file.jsonl
    ├── PHP_code_code_train_file.jsonl
    ├── Python_code_code_train_file.jsonl
    ├── Ruby_code_code_train_file.jsonl
    ├── Rust_code_code_train_file.jsonl
    └── Scala_code_code_train_file.jsonl
```
