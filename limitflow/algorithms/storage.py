import redis
import time

class RedisStore:
    def __init__(self, host='localhost', port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def increment(self, key, window):
        pipe = self.client.pipeline()
        pipe.incr(key, 1)
        pipe.expire(key, window)
        count, _ = pipe.execute()
        return count

    def get(self, key):
        return self.client.get(key)