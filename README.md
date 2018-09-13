# Aggregate deck creator for mtg

Create an aggregate of multiple decklists (for the same flavour of deck), following the [algorithm by Frank Karsten](https://www.channelfireball.com/articles/magic-math-a-new-way-to-determine-an-aggregate-deck-list-rg-dragons/).

## Installation
Clone this repository from github into a directory on your computer. E.g in a bash shell:
```bash
git clone https://github.com/Janna112358/mtg-aggregate.git
```

You should have a directory structure that looks like:
```
.
└── mtg-aggregate       # directory for the python package
    ├── aggregate.py    # python modules 
    ├── deck_reader.py
    ├── ...
    └── __init__.py     # package __init__ file
├── README.md           # what you are reading now
└── setup.py            # important for installation

```
You can install the package (anywhere) using pip
```bash
pip install /path/to/this/directory
```


