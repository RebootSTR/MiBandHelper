# @rebootstr

class Searcher:

    def __init__(self):
        self.value = 0

    def add(self, value: int):
        self.value += value

    def get(self, max: int) -> int:
        if self.value > max:
            return max
        if self.value < 0:
            return 0
        return self.value
