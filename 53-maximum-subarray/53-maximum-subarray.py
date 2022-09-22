class Solution:
    def maxSubArray(self, l: List[int]) -> int:
       
        l2=[]
        current=0
        for i in range(len(l)):
            current=current+l[i]
            if current>0:
                l2.append(current)
            else:
                current=0
        if len(l2)==0:
            return max(l)       
        return max(l2)        

        