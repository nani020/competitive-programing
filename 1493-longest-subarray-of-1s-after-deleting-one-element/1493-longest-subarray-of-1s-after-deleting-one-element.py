class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans =0
        s =0
        low = 0
        for high, num in enumerate(nums):
            s += num
            if s < high - low:
                s = s - nums[low]
                low += 1
            ans = max(ans, high - low)
        return ans
        