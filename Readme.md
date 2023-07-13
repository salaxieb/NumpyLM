## Language model made using only NP

65M parameters LM
speed ~10s/batch

pipeline:
- download dataset
- train tokenizer
- train LM
- inferen

run pipeline:
```bash
python main.py
```

Usefull commands
```bash
poetry install
make lint  # runs linter checkers
make tox  # runs tests in specified python versions
make requirements  # inport poetry requirements to requirements.txt
make clean  # delete chore
```


## This is test project, don't use it in production
todo:
* NewGelu activation layer
* Implement Sophia optimizer