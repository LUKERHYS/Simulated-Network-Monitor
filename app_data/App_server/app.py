import asyncio
import websockets
import json
# from controllers.data_controller import *

import requests
from datetime import datetime

from database import session

if __name__ == '__main__' : 
    def refresh_data():
        fetch = requests.get('http://172.19.0.1:5000/devices/')
        devices = fetch.json()
        for device in devices:
            del device["id"]
            active = device.pop("active_connection")
            upload = device.pop("upload_speed")
            download = device.pop("download_speed")


            found_device = db.session.query(StaticData).filter_by(mac_address=device["mac_address"]).first()
            if found_device:
                static_data_id = found_device.id
            else:
                new_device = StaticData(**device)
                db.session.add(new_device)
                db.session.commit()
                static_data_id = new_device.id

            snapshot = {"static_data_id":static_data_id, "time_stamp": datetime.now(), "active_connection":active, "upload_speed":upload, "download_speed":download}
            dynamic_data = DynamicData(**snapshot)
            db.session.add(dynamic_data)
            db.session.commit()

    DASHBOARDS = set()

    def presentation_data():
        devices = StaticData.query.all()
        
        result = static_data_schema.dumps(devices)
        response = Response(result, status=200, mimetype='application/json')
        return response

    async def notify_dashboards():
        if DASHBOARDS:  # asyncio.wait doesn't accept an empty list
            message = presentation_data()
            await asyncio.wait([dashboard.send(message) for dashboard in DASHBOARDS])

    async def register(websocket):
        DASHBOARDS.add(websocket)
        await notify_dashboards()


    async def unregister(websocket):
        DASHBOARDS.remove(websocket)
        await notify_dashboards()

    async def refresh_dashboards(websocket, path):
        await register(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                if data.type == "refresh":
                    refresh_data()
                    await notify_dashboards()
        finally:
            await unregister(websocket)

    start_server = websockets.serve(refresh_dashboards, port=5001, host='0.0.0.0')

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


