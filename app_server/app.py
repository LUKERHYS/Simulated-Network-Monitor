import asyncio
import websockets

from utils.db import Base, engine
from helpers.data_helper import seed_data
from helpers.socket_helper import runner

if __name__ == '__main__' :
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)

    seed_data(10)

    start_server = websockets.serve(runner, port=5001, host='0.0.0.0')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
s