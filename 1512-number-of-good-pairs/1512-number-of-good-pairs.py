class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        for n,c in count.items():
            res += c*(c-1)//2
        return res    