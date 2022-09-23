class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r,res,total = 0,0,0,0
        while r < len(nums):
            total += nums[r]
            while total + k < (r-l+1) * nums[r]:
                total -= nums[l]
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res
        
   