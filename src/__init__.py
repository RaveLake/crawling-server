import logging

from flask import Flask

app = Flask(__name__)
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    filename='log/flask.log',
    level=logging.INFO
)
