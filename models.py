from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    dbms = db.Column(db.Integer, nullable=False)
    coa = db.Column(db.Integer, nullable=False)
    iwt = db.Column(db.Integer, nullable=False)
    ds = db.Column(db.Integer, nullable=False)
    cpp = db.Column(db.Integer, nullable=False)
