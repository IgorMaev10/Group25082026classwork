import redis
import config

r = redis.Redis(
    host=config.HOST,
    port=config.PORT,
    decode_responses=True,
    username=config.USERNAME,
    password=config.PASSWORD,
)

# r.set('car', 'porsche carrera gt')
# r.set('pet', 'Рися', ex=7200)
# r.lpush('groceries', 'apples', 'milk')
# r.expire('groceries',604800)
# r.hset('recipie', mapping={"flour": "250", "milk": "500"})
# r.hset('recipie', mapping={"sugar": "300"})
# r.hset('recipie', mapping={"sugar": "500"})
