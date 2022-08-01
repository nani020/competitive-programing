class Solution:
    def smallerNumbersThanCurrent(self, n: List[int]) -> List[int]:
        x=len(n)
        c=[0]*x
        for i in range(x):
            for j in range(x):
                if n[i]>n[j]:
                    c[i]+=1
        return c