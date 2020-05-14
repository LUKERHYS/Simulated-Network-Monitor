import asyncio
import websockets

async def refresh():
    uri = "ws://172.19.0.1:5001"
    async with websockets.connect(uri) as websocket:
        await websocket.send("{"type":"refresh"}")

asyncio.get_event_loop().run_until_complete(refresh())
