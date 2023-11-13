class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        y=[]
        l= []
        for i in range(n):
            x.append(nums[i])
        for i in range(n,len(nums)):
            y.append(nums[i])
        for i in range(n):
            l.append(x[i])
            l.append(y[i])
        return l 
        
    
    