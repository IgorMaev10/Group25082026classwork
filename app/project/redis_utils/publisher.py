import time
from redis_utils.redis_client import r

for pub in range(0, 10):
    time.sleep(0.5)
    r.publish('python_channel', f'Hello Redis! Message #{pub}')
