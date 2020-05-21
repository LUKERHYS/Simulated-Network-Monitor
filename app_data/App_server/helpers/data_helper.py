import requests
from datetime import datetime

from utils.db import session
from models.dynamic_data import DynamicData
from models.static_data import StaticData
from schemas.static_data_schema import static_data_schema

def refresh_data():
    fetch = requests.get('http://network:5000/devices/')
    devices = fetch.json()
    for device in devices:
        del device["id"]
        active = device.pop("active_connection")
        upload = device.pop("upload_speed")
        download = device.pop("download_speed")


        found_device = session.query(StaticData).filter_by(mac_address=device["mac_address"]).first()
        if found_device:
            static_data_id = found_device.id
        else:
            new_device = StaticData(**device)
            session.add(new_device)
            session.commit()
            static_data_id = new_device.id

        snapshot = {"static_data_id":static_data_id, "time_stamp": datetime.now(), "active_connection":active, "upload_speed":upload, "download_speed":download}
        dynamic_data = DynamicData(**snapshot)
        session.add(dynamic_data)
        session.commit()

def presentation_data():
    devices = session.query(StaticData).all()
    return static_data_schema.dumps(devices)