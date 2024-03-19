from flask import Flask
from models import *
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Página principal
@app.route("/")
def index():
    return render_template("index")