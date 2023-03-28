# xCodeEval
[xCodeEval: A Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval](https://arxiv.org/abs/2303.03004)

This repository contains the sample code and data link for xCodeEval [paper](https://arxiv.org/abs/2303.03004).


# Data Download

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval
cd xCodeEval
git lfs pull
```
The tree of the data directory is following. It's a total of `124 GB` data.
```
xCodeEval
|── problem_descriptions.jsonl
|── unittest_db.json
├── apr
│   ├── test
│   │   ├── C#.jsonl
│   │   ├── C++.jsonl
│   │   ├── C.jsonl
│   │   ├── Go.jsonl
│   │   ├── Java.jsonl
│   │   ├── Javascript.jsonl
│   │   ├── Kotlin.jsonl
│   │   ├── PHP.jsonl
│   │   ├── Python.jsonl
│   │   ├── Ruby.jsonl
│   │   └── Rust.jsonl
│   ├── train.jsonl
│   └── validation
│       ├── C#.jsonl
│       ├── C++.jsonl
│       ├── C.jsonl
│       ├── Go.jsonl
│       ├── Java.jsonl
│       ├── Javascript.jsonl
│       ├── Kotlin.jsonl
│       ├── PHP.jsonl
│       ├── Python.jsonl
│       ├── Ruby.jsonl
│       └── Rust.jsonl
├── code_compilation
│   ├── test
│   ├── train.jsonl
│   └── validation
├── code-translation
│   ├── test
│   │   ├── C#.jsonl
│   │   ├── C++.jsonl
│   │   ├── C.jsonl
│   │   ├── Go.jsonl
│   │   ├── Java.jsonl
│   │   ├── Javascript.jsonl
│   │   ├── Kotlin.jsonl
│   │   ├── PHP.jsonl
│   │   ├── Python.jsonl
│   │   ├── Ruby.jsonl
│   │   └── Rust.jsonl
│   ├── train.jsonl
│   └── validation
│       ├── C#.jsonl
│       ├── C++.jsonl
│       ├── C.jsonl
│       ├── Go.jsonl
│       ├── Java.jsonl
│       ├── Javascript.jsonl
│       ├── Kotlin.jsonl
│       ├── PHP.jsonl
│       ├── Python.jsonl
│       ├── Ruby.jsonl
│       └── Rust.jsonl
├── program_synthesis
│   ├── test
│   │   └── prog_syn_test.jsonl
│   ├── train.jsonl
│   └── validation
│       └── prog_syn_val.jsonl
├── retrieval
│   ├── C#_code_code_dev_file.jsonl
│   ├── C++_code_code_dev_file.jsonl
│   ├── C_code_code_dev_file.jsonl
│   ├── C#_code_code_test_file.jsonl
│   ├── C++_code_code_test_file.jsonl
│   ├── C_code_code_test_file.jsonl
│   ├── C#_code_code_train_file.jsonl
│   ├── C++_code_code_train_file.jsonl
│   ├── C_code_code_train_file.jsonl
│   ├── C#_code_retrieval_corpus.jsonl
│   ├── C++_code_retrieval_corpus.jsonl
│   ├── C_code_retrieval_corpus.jsonl
│   ├── C#_nl_code_dev_file.jsonl
│   ├── C++_nl_code_dev_file.jsonl
│   ├── C_nl_code_dev_file.jsonl
│   ├── C#_nl_code_test_file.jsonl
│   ├── C++_nl_code_test_file.jsonl
│   ├── C_nl_code_test_file.jsonl
│   ├── C#_nl_code_train_file.jsonl
│   ├── C++_nl_code_train_file.jsonl
│   ├── C_nl_code_train_file.jsonl
│   ├── D_code_code_dev_file.jsonl
│   ├── D_code_code_test_file.jsonl
│   ├── D_code_code_train_file.jsonl
│   ├── D_code_retrieval_corpus.jsonl
│   ├── D_nl_code_dev_file.jsonl
│   ├── D_nl_code_test_file.jsonl
│   ├── D_nl_code_train_file.jsonl
│   ├── Go_code_code_dev_file.jsonl
│   ├── Go_code_code_test_file.jsonl
│   ├── Go_code_code_train_file.jsonl
│   ├── Go_code_retrieval_corpus.jsonl
│   ├── Go_nl_code_dev_file.jsonl
│   ├── Go_nl_code_test_file.jsonl
│   ├── Go_nl_code_train_file.jsonl
│   ├── Haskell_code_code_dev_file.jsonl
│   ├── Haskell_code_code_test_file.jsonl
│   ├── Haskell_code_code_train_file.jsonl
│   ├── Haskell_code_retrieval_corpus.jsonl
│   ├── Haskell_nl_code_dev_file.jsonl
│   ├── Haskell_nl_code_test_file.jsonl
│   ├── Haskell_nl_code_train_file.jsonl
│   ├── Java_code_code_dev_file.jsonl
│   ├── Java_code_code_test_file.jsonl
│   ├── Java_code_code_train_file.jsonl
│   ├── Java_code_retrieval_corpus.jsonl
│   ├── Java_nl_code_dev_file.jsonl
│   ├── Java_nl_code_test_file.jsonl
│   ├── Java_nl_code_train_file.jsonl
│   ├── Javascript_code_code_dev_file.jsonl
│   ├── Javascript_code_code_test_file.jsonl
│   ├── Javascript_code_code_train_file.jsonl
│   ├── Javascript_code_retrieval_corpus.jsonl
│   ├── Javascript_nl_code_dev_file.jsonl
│   ├── Javascript_nl_code_test_file.jsonl
│   ├── Javascript_nl_code_train_file.jsonl
│   ├── Kotlin_code_code_dev_file.jsonl
│   ├── Kotlin_code_code_test_file.jsonl
│   ├── Kotlin_code_code_train_file.jsonl
│   ├── Kotlin_code_retrieval_corpus.jsonl
│   ├── Kotlin_nl_code_dev_file.jsonl
│   ├── Kotlin_nl_code_test_file.jsonl
│   ├── Kotlin_nl_code_train_file.jsonl
│   ├── Ocaml_code_code_dev_file.jsonl
│   ├── Ocaml_code_code_test_file.jsonl
│   ├── Ocaml_code_code_train_file.jsonl
│   ├── Ocaml_code_retrieval_corpus.jsonl
│   ├── Ocaml_nl_code_dev_file.jsonl
│   ├── Ocaml_nl_code_test_file.jsonl
│   ├── Ocaml_nl_code_train_file.jsonl
│   ├── Pascal_code_code_dev_file.jsonl
│   ├── Pascal_code_code_test_file.jsonl
│   ├── Pascal_code_code_train_file.jsonl
│   ├── Pascal_code_retrieval_corpus.jsonl
│   ├── Pascal_nl_code_dev_file.jsonl
│   ├── Pascal_nl_code_test_file.jsonl
│   ├── Pascal_nl_code_train_file.jsonl
│   ├── Perl_code_code_dev_file.jsonl
│   ├── Perl_code_code_test_file.jsonl
│   ├── Perl_code_code_train_file.jsonl
│   ├── Perl_code_retrieval_corpus.jsonl
│   ├── Perl_nl_code_dev_file.jsonl
│   ├── Perl_nl_code_test_file.jsonl
│   ├── Perl_nl_code_train_file.jsonl
│   ├── PHP_code_code_dev_file.jsonl
│   ├── PHP_code_code_test_file.jsonl
│   ├── PHP_code_code_train_file.jsonl
│   ├── PHP_code_retrieval_corpus.jsonl
│   ├── PHP_nl_code_dev_file.jsonl
│   ├── PHP_nl_code_test_file.jsonl
│   ├── PHP_nl_code_train_file.jsonl
│   ├── Python_code_code_dev_file.jsonl
│   ├── Python_code_code_test_file.jsonl
│   ├── Python_code_code_train_file.jsonl
│   ├── Python_code_retrieval_corpus.jsonl
│   ├── Python_nl_code_dev_file.jsonl
│   ├── Python_nl_code_test_file.jsonl
│   ├── Python_nl_code_train_file.jsonl
│   ├── Ruby_code_code_dev_file.jsonl
│   ├── Ruby_code_code_test_file.jsonl
│   ├── Ruby_code_code_train_file.jsonl
│   ├── Ruby_code_retrieval_corpus.jsonl
│   ├── Ruby_nl_code_dev_file.jsonl
│   ├── Ruby_nl_code_test_file.jsonl
│   ├── Ruby_nl_code_train_file.jsonl
│   ├── Rust_code_code_dev_file.jsonl
│   ├── Rust_code_code_test_file.jsonl
│   ├── Rust_code_code_train_file.jsonl
│   ├── Rust_code_retrieval_corpus.jsonl
│   ├── Rust_nl_code_dev_file.jsonl
│   ├── Rust_nl_code_test_file.jsonl
│   ├── Rust_nl_code_train_file.jsonl
│   ├── Scala_code_code_dev_file.jsonl
│   ├── Scala_code_code_test_file.jsonl
│   ├── Scala_code_code_train_file.jsonl
│   ├── Scala_code_retrieval_corpus.jsonl
│   ├── Scala_nl_code_dev_file.jsonl
│   ├── Scala_nl_code_test_file.jsonl
│   └── Scala_nl_code_train_file.jsonl
└── tag_classification
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

# Citation

```
@misc{khan2023xcodeeval,
      title={xCodeEval: A Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval}, 
      author={Mohammad Abdullah Matin Khan and M Saiful Bari and Xuan Long Do and Weishi Wang and Md Rizwan Parvez and Shafiq Joty},
      year={2023},
      eprint={2303.03004},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

