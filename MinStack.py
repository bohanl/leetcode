class MinStack:
    def __init__(self):
        self.s1, self.s2 = [], []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.s1.append(x)
        if not self.s2 or x <= self.s2[-1]:
            self.s2.append(x)

    # @return nothing
    def pop(self):
        x = self.s1.pop()
        if x == self.s2[-1]:
            self.s2.pop()

    # @return an integer
    def top(self):
        return self.s1[-1] if self.s1 else None

    # @return an integer
    def getMin(self):
        return self.s2[-1] if self.s2 else None