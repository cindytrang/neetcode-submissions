class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        values = self.values
        values.append(val)
        self.values = values

    def pop(self) -> None:
        values =  self.values
        last = values[len(self.values)-1]
        updated = values[:len(self.values)-1]
        self.values = updated
        return last 

    def top(self) -> int:
        values =  self.values
        last = values[len(self.values)-1]
        return last 

    def getMin(self) -> int:
        values = self.values
        return min([i for i in values])
        
