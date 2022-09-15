class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        x=len(nums)
        for i in range(x):
            nums[i] = nums[i] + sum
            sum = nums[i]
        return nums