import asyncio
import websockets
import json
import logging
import requests
from datetime import datetime

from utils.db import Base, engine, session
from models.dynamic_data import DynamicData
from models.static_data import StaticData
from schemas.static_data_schema import static_data_schema
from helpers.data_helper import seed_data, presentation_data
from helpers.socket_helper import runner

if __name__ == '__main__' :
    logging.basicConfig()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)

    seed_data(10)

    start_server = websockets.serve(runner, port=5001, host='0.0.0.0')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
s