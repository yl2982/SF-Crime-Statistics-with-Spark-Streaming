import asyncio

from confluent_kafka import Consumer


async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'PLAINTEXT://localhost:9092',
        'group.id': 0,
    })

    consumer.subscribe(['com.udacity.police.service'])

    while 1:
        messages = consumer.consume(3, timeout=1)

        for message in messages:
            if message is None:
                print('Message not found...\n\n')
            elif message.error() is not None:
                print(f'ERROR: {message.error()}\n\n')
            else:
                print(f'{message.value()}\n\n')

        await asyncio.sleep(1)


if __name__ == '__main__':
    try:
        asyncio.run(consume("com.udacity.police.service"))
    except Exception as e:
        print("Shutting down...")