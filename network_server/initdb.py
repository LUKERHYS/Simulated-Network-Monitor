import os 

from utils.app_factory import create_app
from utils.db import db

from models.device import Device
from seeds.seeds import device_data

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    for device in device_data:
        new_device = Device(**device)
        db.session.add(new_device)
    db.session.commit()   

print("Database initialized...")
