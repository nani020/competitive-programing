class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        s=0
        for i in pushed:
            stack.append(i) #we are pushing the number to the stack
            while  len(stack) >0 and stack[len(stack)-1] == popped[s] :
                stack.pop()
                s+=1
        return True if len(stack) ==0 else False