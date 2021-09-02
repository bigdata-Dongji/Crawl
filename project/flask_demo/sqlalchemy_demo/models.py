from app import db
class Wealth(db.Model):
    __tablename__ = "wealth"   #表名
    rank = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    wealth = db.Column(db.String(255))
    sourse = db.Column(db.String(255))
    region = db.Column(db.String(255))