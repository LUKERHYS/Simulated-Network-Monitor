import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested

Base = declarative_base()
basedir = os.path.abspath((os.path.dirname(__file__)))
sqlalchemy_db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
engine = create_engine(sqlalchemy_db_uri)
session = scoped_session(sessionmaker(bind=engine))

class DynamicData(Base):
    __tablename__ = 'dynamic_data'
    id = Column(Integer, primary_key = True)
    static_data_id = Column(Integer, ForeignKey('static_data.id'), nullable=False)
    static_data = relationship('StaticData', back_populates='snap_shots')
    time_stamp = Column(String(255))
    upload_speed = Column(Integer)
    download_speed = Column(Integer)
    active_connection = Column(Boolean)

class StaticData(Base):
    __tablename__ = 'static_data'
    id = Column(Integer, primary_key = True)
    host_name = Column(String(255))
    device_type = Column(String(255))
    operating_system = Column(String(255))
    mac_address = Column(String(255), unique=True)
    ip_address = Column(String(255))
    snap_shots = relationship('DynamicData', back_populates='static_data')

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

# Test data
# static = StaticData(host_name ="a", device_type="b", operating_system="c", mac_address="d", ip_address="e")
# session.add(static)
# session.commit()
# dynamic = DynamicData(static_data_id=static.id, time_stamp="aaa", upload_speed=0, download_speed=0, active_connection=False)
# session.add(dynamic)
# session.commit()

# all_devices = session.query(StaticData).all()
# data = static_data_schema.dumps(all_devices)
# print(data)