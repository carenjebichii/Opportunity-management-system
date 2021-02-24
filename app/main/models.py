from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin
from app import db

from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, index=True)
    username = db.Column(db.String(80), unique=True)
    phone_number = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<User {}".format(self.email)


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<Account {}".format(self.name)



class Opportunity(db.Model):
    __tablename__ = "opportunities"

    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer)


class Stage(db.Model):
    __tablename__ = "stages"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True,index=True)

    def __repr__(self):
        return "<Stage {}".format(self.name)


