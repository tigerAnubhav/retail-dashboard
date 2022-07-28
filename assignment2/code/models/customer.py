from db import db


class CustomerModel(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    @classmethod
    def find_by_usename(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"fname": self.fname, "lname": self.lname, "username": self.username}
