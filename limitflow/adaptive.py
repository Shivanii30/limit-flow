class AdaptiveLimiter:
    def __init__(self, base_limit):
        self.base_limit = base_limit

    def adjust_limit(self, current_rate):
        if current_rate > self.base_limit * 1.5:
            return int(self.base_limit * 0.7)  # tighten
        elif current_rate < self.base_limit * 0.5:
            return int(self.base_limit * 1.2)  # relax
        return self.base_limit