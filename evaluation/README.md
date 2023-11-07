# How to perform evaluation using ExecEval

## Configure ExecEval

Follow the instrauction [here](https://github.com/ntunlp/execeval).

> :warning: ❌ Do not run ExecEval without Docker image

`Java` and `Kotlin 1.5` has a lots of Memory related issue. If you don't have large amount of memory please reduce the multiple worker. If you are running in a laptop or Desktop with limited amount of RAM (~ 32 GB), please use num `NUM_WORKERS`=1.

## Generate samples

Generate samples using OpenAI api.

```
python evaluation/program_synthesis/gen_program_synthesis.py
```

## Eval Samples using ExecEval

Keep ExecEval server/endpoint running and then run the following code, 

```
python evaluation/program_synthesis/eval_program_synthesis.py
```

## Calculate pass@k

Calculate pass@k by the following script,

```
python evaluation/program_synthesis/get_result.py
```