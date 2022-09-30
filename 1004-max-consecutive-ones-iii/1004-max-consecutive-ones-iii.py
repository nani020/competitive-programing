class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ll=0
        for r,n in enumerate(nums):
            k-=(1-n)
            if k< 0:
                k+=(1-nums[ll])
                ll+=1
        return r-ll+1
    