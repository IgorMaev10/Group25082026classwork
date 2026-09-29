from redis_utils.redis_client import r

subscriber = r.pubsub()
subscriber.subscribe("python_channel")

for message in subscriber.listen():
    print(message)
