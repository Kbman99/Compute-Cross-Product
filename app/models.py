from .core import db
from sqlalchemy.dialects.postgresql import ARRAY, NUMERIC

import datetime


class ResultList(db.Model):
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2
        self.created = datetime.datetime.now()
        self.result = self.calc_result()

    __tablename__ = 'result_list'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vector1 = db.Column(ARRAY(db.Numeric))
    vector2 = db.Column(ARRAY(db.Numeric))
    result = db.Column(ARRAY(db.Numeric))
    created = db.Column(db.DateTime, nullable=False)

    def calc_result(self):
        return [self.vector1[1] * self.vector2[2] - self.vector1[2] * self.vector2[1],
                self.vector1[2] * self.vector2[0] - self.vector1[0] * self.vector2[2],
                self.vector1[0] * self.vector2[1] - self.vector1[1] * self.vector2[0]]


class Result(db.Model):
    """ Holds vector values in separate objects for simple storage """
    def __init__(self, v1, v2, cp):
        self.vector_one_x = v1[0]
        self.vector_one_y = v1[1]
        self.vector_one_z = v1[2]
        self.vector_two_x = v2[0]
        self.vector_two_y = v2[1]
        self.vector_two_z = v2[2]
        self.cross_product_x = cp[0]
        self.cross_product_y = cp[1]
        self.cross_product_z = cp[2]
        self.created = datetime.datetime.now()

    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True)
    vector_one_x = db.Column(db.Integer)
    vector_one_y = db.Column(db.Integer)
    vector_one_z = db.Column(db.Integer)
    vector_two_x = db.Column(db.Integer)
    vector_two_y = db.Column(db.Integer)
    vector_two_z = db.Column(db.Integer)
    cross_product_x = db.Column(db.Integer)
    cross_product_y = db.Column(db.Integer)
    cross_product_z = db.Column(db.Integer)
    created = db.Column(db.DateTime, nullable=False)

    @property
    def result(self):
        return 'The cross product of [{}, {}, {}] and [{}, {}, {}] is [{}, {}, {}]'.format(
            self.vector_one_x, self.vector_one_y, self.vector_one_z,
            self.vector_two_x, self.vector_two_y, self.vector_two_z,
            self.cross_product_x, self.cross_product_y, self.cross_product_z)

    def get_id(self):
        return self.id
