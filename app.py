from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'slozhniy-parol'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from routes import *
from models import User


if __name__ == '__main__':
    app.run(port='8080', debug=True)
