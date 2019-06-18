from datetime import datetime
from . import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.now)
