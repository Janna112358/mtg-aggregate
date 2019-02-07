# activates venv called web_venv
. web_venv/bin/activate
# installs requirements
pip install -r requirements.txt
# set the FLASK_APP environment var to the name of the app
export FLASK_APP=mtg_app.py
