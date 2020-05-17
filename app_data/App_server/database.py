import os
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested

from models.dynamic_data import DynamicData
from models.static_data import StaticData

from utils.db import Base, session, engine

class DynamicDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DynamicData

dynamic_data_schema = DynamicDataSchema(many=True)   

class StaticDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StaticData
        include_relationships = True
    snap_shots = Nested(DynamicDataSchema(many=True))

static_data_schema = StaticDataSchema(many=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)