from utils.db import db
from models.dynamic_data import DynamicData

class StaticData(db.Model):
    __tablename__ = 'static_data'
    id = db.Column(db.Integer, primary_key = True)
    host_name = db.Column(db.String(255))
    device_type = db.Column(db.String(255))
    operating_system = db.Column(db.String(255))
    mac_address = db.Column(db.String(255), unique=True)
    ip_address = db.Column(db.String(255))
    snap_shots = db.relationship('DynamicData', back_populates='static_data')
