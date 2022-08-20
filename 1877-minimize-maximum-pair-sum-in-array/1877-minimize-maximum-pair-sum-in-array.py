class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = []
        for i in range(len(nums)):
            sums.append(nums[i] + nums[-i-1])
        return max(sums)
      