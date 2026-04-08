class FixedWindow:
    def __init__(self, limit, window, store):
        self.limit = limit
        self.window = window
        self.store = store

    def is_allowed(self, key):
        count = self.store.increment(key, self.window)
        return count <= self.limit
