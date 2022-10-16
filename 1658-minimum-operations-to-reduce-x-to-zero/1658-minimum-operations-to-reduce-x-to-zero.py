class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # find the longest subarray that sum to 'goal'
        s = sum(nums)
        n = len(nums)
        goal = s - x
        max_length = -1
        left = 0
        current_sum = 0

        for right, num in enumerate(nums):
            current_sum += num
            # if larger, move `left` to right
            while current_sum > goal and left <= right:
                current_sum -= nums[left]
                left += 1
            # check if equal
            if current_sum == goal:
                max_length = max(max_length, right-left+1)

        return n - max_length if max_length != -1 else -1        