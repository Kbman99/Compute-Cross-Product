from sqlalchemy.dialects.postgresql import ARRAY
import datetime

from app.core import db


class ResultList(db.Model):
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2
        self.created = datetime.datetime.now()
        self.result = self.calc_result()

    __tablename__ = 'cross_product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vector1 = db.Column(ARRAY(db.Numeric))
    vector2 = db.Column(ARRAY(db.Numeric))
    result = db.Column(ARRAY(db.Numeric))
    created = db.Column(db.DateTime, nullable=False)

    def calc_result(self):
        return [self.vector1[1] * self.vector2[2] - self.vector1[2] * self.vector2[1],
                self.vector1[2] * self.vector2[0] - self.vector1[0] * self.vector2[2],
                self.vector1[0] * self.vector2[1] - self.vector1[1] * self.vector2[0]]
