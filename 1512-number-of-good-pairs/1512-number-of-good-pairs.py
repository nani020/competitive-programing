class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        X=[]
        y=len(nums)
        for i in range(y):
            for j in range(i+1,y):
                if nums[i]==nums[j]:
                    X.append((i,j))
        return len(X)
        