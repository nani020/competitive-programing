class MyQueue(object):

    def __init__(self):
  
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x):
       
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self):
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        
        return ans

    def peek(self):
        
        if self.stack2:
            return self.stack2[-1]
        
        return self.front

    def empty(self):
        
        return (not self.stack1 and not self.stack2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
