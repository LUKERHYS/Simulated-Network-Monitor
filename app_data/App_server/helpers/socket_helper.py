import asyncio
import websockets
import logging

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
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)