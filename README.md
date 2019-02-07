# Aggregate deck creator for mtg

Create an aggregate of multiple decklists (for the same flavour of deck), following the [algorithm by Frank Karsten](https://www.channelfireball.com/articles/magic-math-a-new-way-to-determine-an-aggregate-deck-list-rg-dragons/).

## Installation
This is for the installation of the python package for the aggregate code. There is also a package for the web app (in development, see below).
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
└── mtg_agg_web         # directory for the web app (not needed to install the python package)
    ├── mtg-agg-web     # web app python package
    └── ...
├── ...
├── README.md           # what you are reading now
└── setup.py            # important for installation

```
You can install the package (anywhere) using pip
```bash
pip install /path/to/this/directory
```

## The web app
In this repositery there is a python package for a flask web app (in development), which can be found in the directory structure:
```
.
├──mtg-aggregate         # directory for the python package (assumeing you have this installed, see above)
└── mtg_agg_web          # directory for the web app
    ├── mtg-agg-web      # web app python package
    ├── requirements.txt 
    └── setup_env.sh     # activates virtual env and installs flask
├── ... 
└── README.md            # what you are reading now

```
### Setup web_venv with flask
The web app in build on flask, which we want to install only in a virtual environment. So first, go to the `mtg_agg_web` directory and make a virtual env called `web_venv`:
```bash
cd mtg_agg_web
python3 -m venv web_venv
```
Then, you can activate web_venv and install flask etc automatically using requirements.txt. This also sets the environment variable `FLASK_APP` so that flask can find the app to run:
```bash
./setup_env.sh
```
You're now in the virtual environment. The terminal shows this by starting the command line with `(web_env)`. You can exit it with:
```bash
deactivate
```
Should you want to delete the virtual enviroment simply:
```bash
rm -rf web_venv
```

### Run the web app
To run the web app, go the the `mtg-agg-web` directory (which is the python package) and run flask:
```bash
cd mtg-agg-web
flask run
```
Flask comes up with a link which you can open in your web browser. You can quit with `ctrl+c`.
