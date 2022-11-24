class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in enumerate(d):
            if d[j]==1:
                return j