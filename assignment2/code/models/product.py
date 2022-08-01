from db import db


class ProductModel(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    product_des = db.Column(db.String(50))

    def __int__(self, product_id, product_des):
        self.product_id = product_id
        self.product_des = product_des

    def json(self):
        return {"product_id": self.product_id, "product_des": self.product_des}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
