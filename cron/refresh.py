#!/usr/bin/python3
import asyncio
import websockets
import json

print("hello")
async def refresh():
    uri = "ws://app:5001/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"socket_type": "refresh"}))
        await websocket.close()

asyncio.get_event_loop().run_until_complete(refresh())
