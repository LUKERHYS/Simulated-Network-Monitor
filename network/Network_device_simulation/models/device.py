import random
from utils.db import db

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key = True)
    host_name = db.Column(db.String(255))
    device_type = db.Column(db.String(255))
    operating_system = db.Column(db.String(255))
    mac_address = db.Column(db.String(255), unique=True)
    ip_address = db.Column(db.String(255))
    upload_speed = db.Column(db.Integer)
    download_speed = db.Column(db.Integer)
    active_connection = db.Column(db.Boolean)

    def __init__(self, host_name, device_type, operating_system, mac_address, ip_address, upload_speed, download_speed, active_connection):
        self.host_name = host_name
        self.device_type = device_type
        self.operating_system = operating_system
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.upload_speed = upload_speed
        self.download_speed = download_speed
        self.active_connection = active_connection

    def update(self):
        self.update_active_connection()
        self.update_upload_download()

        db.session.commit()

    def update_active_connection(self):
        if random.randint(1,5) > 4:
            self.active_connection = not self.active_connection
    
    def update_upload_download(self):
        if self.active_connection:       
            self.upload_speed = random.randint(0, 12)
            self.download_speed = random.randint(0, 70)
        else:
            self.upload_speed = 0 
            self.download_speed = 0