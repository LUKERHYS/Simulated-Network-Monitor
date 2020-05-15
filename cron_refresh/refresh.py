#!/usr/bin/python3
import asyncio
import websockets
import json

print("hello")
async def refresh():
    uri = "ws://172.18.0.1:5001/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"socket_type": "refresh"}))

asyncio.get_event_loop().run_until_complete(refresh())
