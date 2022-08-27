class MyQueue:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def peek(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        return len(self.q)==0

	
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue:

		def __init__(self):
			self.queue = []

		def push(self, x: int) -> None:
			self.queue.append(x)

		def pop(self) -> int:
			return self.queue.pop(0)

		def peek(self) -> int:
			return self.queue[0]

		def empty(self) -> bool:
			""" 
			pythonのリストは何か入っていると、Trueとして扱われる
			[] （空リスト）だとFalse
			"""
		
			if self.queue:
				return False

			return True