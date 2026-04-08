from fastapi import Request, HTTPException

class RateLimiter:
    def __init__(self, algorithm, key_func):
        self.algorithm = algorithm
        self.key_func = key_func

    async def __call__(self, request: Request):
        key = self.key_func(request)

        path = request.url.path

        if hasattr(self.algorithm, 'is_allowed'):
            try:
                allowed = await self.algorithm.is_allowed(key, path)
            except TypeError:
                allowed = self.algorithm.is_allowed(key, path)
        else:
                allowed = self.algorithm(key, path)

        if not allowed:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")