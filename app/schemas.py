import simplejson
from marshmallow import validate, fields, ValidationError

from app.models import ResultList
from app.core import ma


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


class ValidationSchema(ma.Schema):
    """ Validates against all incoming POST requests """
    class Meta:
        fields = ('vector1', 'vector2')
    vector1 = ma.List(StrictNumber(), required=True, validate=length_of)
    vector2 = ma.List(StrictNumber(), required=True, validate=length_of)


class ResultListSchema(ma.ModelSchema):
    """ Used to dump result objects into a response """
    class Meta:
        model = ResultList
        json_module = simplejson
    id = ma.Integer()
    vector1 = ma.List(fields.Decimal(), required=True, validate=length_of)
    vector2 = ma.List(fields.Decimal(), required=True, validate=length_of)
    result = ma.List(fields.Decimal(), required=True, validate=length_of)
    created = ma.DateTime()


class AllResultsListSchema(ma.Schema):
    """ Used to dump a list of result objects into a response """
    results = ma.Nested('ResultListSchema', many=True)
