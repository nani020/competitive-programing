class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        p = 0
        for i in range(N-1,0,-1):
            if nums[i-1] < nums[i]:
                p = i
                break
        if p == 0:
            nums.sort()
            return

        swap = N-1
        while nums[p-1] >= nums[swap]:
            swap-=1
        nums[swap],nums[p-1] = nums[p-1],nums[swap]
        nums[p:] = reversed(nums[p:])
        