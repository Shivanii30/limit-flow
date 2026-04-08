from fastapi import FastAPI, Depends, Request
from limitflow.limiter import RateLimiter
from limitflow.storage import RedisStore

# Import algorithms
from limitflow.algorithms.fixed_window import FixedWindow
from limitflow.algorithms.sliding_window import SlidingWindow
from limitflow.algorithms.token_bucket import TokenBucket
from limitflow.cost_limiter import CostBasedLimiter
from limitflow.waf import WAFEscalation
app = FastAPI()

store = RedisStore()

# 🔁 CHANGE THIS LINE TO TEST DIFFERENT ALGORITHMS

algo = FixedWindow(limit=100, window=60, store=store)
#algo = SlidingWindow(limit=100, window=60, store=store)

cost_map = {
    "/" : 1,
    "/heavy": 20
}

base_algo = TokenBucket(capacity=800, refill_rate=20, store=store)
algo = CostBasedLimiter(base_algo, cost_map)
algo = WAFEscalation(algo)

def get_user(request: Request):
    return request.headers.get("X-User", request.client.host)

limiter = RateLimiter(algo, get_user)

@app.get("/")
async def home(dep=Depends(limiter)):
    return {"message": "Hello, limitflow!"}

@app.get("/heavy")
async def heavy(dep=Depends(limiter)):
    return {"message": "This is expensive!"}