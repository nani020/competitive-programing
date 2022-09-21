class Solution:
    def pivotIndex(self, l: List[int]) -> int:
        right=sum(l)
        left=0
        for i in range(len(l)):
            right-=l[i]
            if right==left:
                return i
            left+=l[i]
        return -1    
            