from utils.db import db

class DynamicData(db.Model):
    __tablename__ = 'dynamic_data'
    id = db.Column(db.Integer, primary_key = True)
    static_data_id = db.Column(db.Integer, db.ForeignKey('static_data.id'), nullable=False)
    static_data = db.relationship('StaticData', back_populates='snap_shots')
    time_stamp = db.Column(db.String(255))
    upload_speed = db.Column(db.Integer)
    download_speed = db.Column(db.Integer)
    active_connection = db.Column(db.Boolean)
