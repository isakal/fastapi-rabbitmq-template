import string
import random
from fastapi import FastAPI
from mq_client import MQClient
from contextlib import asynccontextmanager


mq_cl = MQClient()

@asynccontextmanager
async def lifespan(_: FastAPI):
    # everything before yield is executed before the app starts up
    # everything after yield is execute after the app shuts down
    await mq_cl.connect()
    await mq_cl.consume("a_queue")
    yield
    await mq_cl.disconnect()


app = FastAPI(lifespan=lifespan)


@app.api_route("/")
async def home():
    txt = "".join(random.choices(string.ascii_letters, k=4))
    await mq_cl.send_message({
        "random_id": txt
    })
    print(f"SENT: {txt}", flush=True)

    return {
        "hello": "world"
    }
