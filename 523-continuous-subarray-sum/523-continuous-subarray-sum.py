class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem={0:-1}
        total=0
        for i,n in enumerate(nums):
            total+=n
            r=total%k
            if r not in rem:
                rem[r]=i
            elif i - rem[r]>1:
                return True
        return False   
        