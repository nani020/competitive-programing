class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        t=0
        
        res=float('inf')
        for i in range(len(nums)):
            t+=nums[i]
            while t>=target:
                res=min(res,i-l+1)
                t-=nums[l]
                l+=1
        if res==float('inf'):
            return 0
        else:
            return res
    