import time

class TokenBucket:
    def __init__(self, capacity, refill_rate, store):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.store = store

    def allow_request(self, key):
        redis_key = f"tb:{key}"

        data = self.store.client.hgetall(redis_key)

        now = time.time()

        tokens = float(data.get("tokens", self.capacity))
        last_refill = float(data.get("last_refill", now))

        elapsed = now - last_refill
        tokens = min(self.capacity, tokens + elapsed * self.refill_rate)

        if tokens >= 1:
            tokens -= 1
            allowed = True
        else:
            allowed = False

        self.store.client.hset(redis_key, mapping={
            "tokens": tokens,
            "last_refill": now
        })

        self.store.client.expire(redis_key, 60)

        return allowed