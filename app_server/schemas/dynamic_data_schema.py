from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from models.dynamic_data import DynamicData

class DynamicDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DynamicData

dynamic_data_schema = DynamicDataSchema(many=True)   