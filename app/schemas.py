from app.core import ma
from marshmallow import validate, fields, ValidationError


length_of = validate.Length(equal=3, error='Field must be of length 3.')


class StrictNumber(fields.Integer):
    """ Override fields.Number string to num coercion"""
    def _format_num(self, value):
        """Check if instance of int or float or raise a :exc:`ValidationError` if an error occurs."""
        if value is None:
            return None
        if not isinstance(value, (self.num_type, float)):
            raise ValidationError("Must be of type int or float")
        return value


class ValidateSchema(ma.Schema):
    """ Validates against all incoming POST requests """
    class Meta:
       fields = ('vector1', 'vector2')
    vector1 = ma.List(StrictNumber(), required=True, validate=length_of)
    vector2 = ma.List(StrictNumber(), required=True, validate=length_of)


class ResultListSchema(ma.Schema):
    """ Used to dump result objects into a response """
    id = ma.Integer()
    vector1 = ma.List(StrictNumber(), required=True, validate=length_of)
    vector2 = ma.List(StrictNumber(), required=True, validate=length_of)
    result = ma.List(StrictNumber(), required=True, validate=length_of)
    created = ma.DateTime()


class AllResultsListSchema(ma.Schema):
    """ Used to dump a list of result objects into a response """
    results = ma.Nested('ResultListSchema', many=True)


class ResultSchema(ma.Schema):
    id = ma.Integer()
    vector1 = ma.Nested('self', only='val', many=True)
    vector2 = ma.Nested('self', only='val', many=True)
    result = ma.Nested('self', only='val', many=True)
    created = ma.DateTime()


class AllResultsSchema(ma.Schema):
    results = ma.Nested('ResultSchema', many=True)
