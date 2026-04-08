from importlib.resources import path
import time


class WAFEscalation:
    def __init__(self, base_limiter):
        self.base_limiter = base_limiter

        # track violations per user
        self.violations = {}

        # config
        self.warn_threshold = 3
        self.limit_threshold = 6
        self.block_threshold = 10

        self.block_time = 60  # seconds
    
    def __call__(self, key, path=None):
        return self.allow_request(key, path)

    def allow_request(self, key, path=None):
        now = time.time()

        user = self.violations.get(key, {
            "count": 0,
            "blocked_until": 0
        })

        # 🔴 If user is blocked
        if now < user["blocked_until"]:
            return False

        # ✅ Try base limiter first
        allowed = self.base_limiter.allow_request(key, path)

        if allowed:
            return True

        # ❌ If request failed → increase violations
        user["count"] += 1

        # 🟡 Escalation logic
        if user["count"] > self.block_threshold:
            user["blocked_until"] = now + self.block_time
            print(f"[WAF] User: {key} is BLOCKED until {time.ctime(user['blocked_until'])}")

        elif user["count"] > self.limit_threshold:
            # make limiter stricter (reduce capacity)
            if hasattr(self.base_limiter.base_algo, "capacity"):
                self.base_limiter.base_algo.capacity = max(
                    10,
                    self.base_limiter.base_algo.capacity // 2
                )

        elif user["count"] > self.warn_threshold:
            # just warning (no action yet)
            pass

        self.violations[key] = user
        print(f"[WAF] User: {key}, Violations: {user['count']}, Blocked_until: {user['blocked_until']}")

        return False