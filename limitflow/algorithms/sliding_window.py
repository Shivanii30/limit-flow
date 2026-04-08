import time

class SlidingWindow:
    def __init__(self, limit, window, store):
        self.limit = limit
        self.window = window
        self.store = store

    def allow_request(self, key):
        now = time.time()
        window_start = now - self.window

        redis_key = f"sw:{key}"

        # Add current request
        self.store.client.zadd(redis_key, {now: now})

        # Remove old requests
        self.store.client.zremrangebyscore(redis_key, 0, window_start)

        # Count current requests
        count = self.store.client.zcard(redis_key)

        self.store.client.expire(redis_key, self.window)

        return count <= self.limit