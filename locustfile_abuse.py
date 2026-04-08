from locust import HttpUser, task, between
import random

class RateLimitUser(HttpUser):
    # Very aggressive → simulates bots
    wait_time = between(0.01, 0.02)

    @task
    def hit_api(self):
        user_id = random.randint(1, 5)
        self.client.get("/", headers={"X-User": str(user_id)})