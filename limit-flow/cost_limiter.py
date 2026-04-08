class CostBasedLimiter:
    def __init__(self, base_algo, cost_map):
        """
        base_algo: your existing algorithm (TokenBucket / SlidingWindow / FixedWindow)
        cost_map: dict of endpoint → cost
        """
        self.base_algo = base_algo
        self.cost_map = cost_map
    
    def __call__(self, key, path):
        return self.allow_request(key, path)

    def get_cost(self, path):
        return self.cost_map.get(path, 1)  # default cost = 1

    def allow_request(self, key, path):
        cost = self.get_cost(path)

        # consume multiple tokens based on cost
        for _ in range(cost):
            if not self.base_algo.allow_request(key):
                return False

        return True