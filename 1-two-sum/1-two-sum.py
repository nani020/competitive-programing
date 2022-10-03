class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for key in range(len(nums)-1):
            if (target-nums[key]) in nums[key+1:]:
                return key,nums.index(target-nums[key],key+1)