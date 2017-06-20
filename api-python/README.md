## Environment

* Python 3.6
* Up-to-date [`pip`](https://pip.pypa.io/en/stable/)
* [Optional, Recommended] Use of a [`virtualenv`](https://virtualenv.pypa.io/en/stable/)

## Setup and Run

1. Install Python level dependencies `$ pip install -r requirements.txt`
2. Run `$ SQL_URI=<SQL connection URI> FLASK_APP=app.py FLASK_DEBUG=1 flask run` and by default it should now be listening on port `5000`.
3. Open your browser and point to `localhost:5000` and you should see `Welcome to EQ Works 😎`

_Note_: you'll be given necessary `SQL_URI` value along with the problem set
