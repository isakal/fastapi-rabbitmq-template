import asyncio
from aio_pika import connect, IncomingMessage
import json


async def on_msg(msg: IncomingMessage):
    msg_text =  json.loads(
        msg.body.decode("utf-8")
    )

    print("got a message")

    # processing
    print("processing message")
    await asyncio.sleep(10)
    
    print(msg_text)
    
    
    print("acking")
    await msg.ack()    


async def main():
    connection = await connect("amqp://user:password@mq:5672/")

    channel = await connection.channel(publisher_confirms=False)

    queue = await channel.declare_queue("b_queue")

    await queue.consume(callback=on_msg)

    print("---")
    print("waiting for messages")
    print("---")

    await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
