import asyncio
import websockets
import logging
import json

from helpers.data_helper import refresh_data, presentation_data, number_of_snapshots, clear_data, seed_data

DASHBOARDS = set()

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

async def runner(websocket, path):   
    await register(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            if data["socket_type"] == "refresh":
                refresh_data()
                await notify_dashboards()
                if number_of_snapshots() >= 60:
                    clear_data()
                    seed_data(10)
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)