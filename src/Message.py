import numpy as np

class Message:
    def __init__(self, content):
        self.content = content
        self.id = np.random.randint(2147483647, 9223372036854775807, size=1, dtype=np.int64)[0]
