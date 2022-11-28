from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b982c2edf1a2f17e9e06c49fb027e8d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uzdzjw3pk85zapxpmxqv:f4DYUR6MaBhN1Bsvl0Bz@bxyuyemtcjfheoyq7tj6-postgresql.services.clever-cloud.com:5432/bxyuyemtcjfheoyq7tj6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in' 
login_manager.login_message_category = 'info'


from app import routes
