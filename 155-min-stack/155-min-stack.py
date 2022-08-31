class MinStack:

    def __init__(self):
        self.storage=[]
        

    def push(self, val: int) -> None:
        self.storage.append(val)
        

    def pop(self) -> None:
        if len(self.storage):
            self.storage.pop()
        

    def top(self) -> int:
        return self.storage[-1]
        

    def getMin(self) -> int:
        return min(self.storage)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()