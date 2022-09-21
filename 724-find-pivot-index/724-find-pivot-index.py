class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps=[nums[0]]*len(nums)    
    
        for i in range(1,len(nums)):
            ps[i]=ps[i-1]+nums[i]
        for i in range(len(nums)):
            left=ps[i]-nums[i]
            right=ps[-1]-ps[i]
            if left==right:
                return i
        return -1