from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested

from models.static_data import StaticData
from schemas.dynamic_data_schema import dynamic_data_schema

class StaticDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StaticData
        include_relationships = True
    snap_shots = Nested(dynamic_data_schema)

static_data_schema = StaticDataSchema(many=True)