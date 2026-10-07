class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.prefix or val <= self.prefix[-1]:
            self.prefix.append(val)
        return

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.getMin():
            self.prefix.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
        