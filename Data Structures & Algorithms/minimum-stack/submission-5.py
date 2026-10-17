class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        self.values.append(val)

    def pop(self) -> None:
        return self.values.pop()

    def top(self) -> int: # -1 gets the last element
        return self.values[-1]

    def getMin(self) -> int:
        values = self.values
        return min([i for i in values])
        
