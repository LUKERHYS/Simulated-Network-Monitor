import asyncio
import websockets
import json
import logging

logging.basicConfig()

import requests
from datetime import datetime
from utils.db import session
from models.dynamic_data import DynamicData
from models.static_data import StaticData
from schemas.static_data_schema import static_data_schema

from utils.db import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)

if __name__ == '__main__' : 
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

    DASHBOARDS = set()

    def presentation_data():
        devices = session.query(StaticData).all()
        return static_data_schema.dumps(devices)

    async def notify_dashboards():
        if DASHBOARDS:
            message = presentation_data()
            await asyncio.wait([dashboard.send(message) for dashboard in DASHBOARDS])

    async def register(websocket):
        DASHBOARDS.add(websocket)
        message = presentation_data()
        await websocket.send(message)

    async def unregister(websocket):
        DASHBOARDS.remove(websocket)

    async def refresher(websocket, path):   
        await register(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                if data["socket_type"] == "refresh":
                    refresh_data()
                    await notify_dashboards()
                else:
                    logging.error("unsupported event: {}", data)
        finally:
            await unregister(websocket)
    
    refresh_data()

    start_server = websockets.serve(refresher, port=5001, host='0.0.0.0')

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
