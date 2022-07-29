class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=[]
        b=[]
        for i in nums:
            a.append(int(i))
        a.sort()
        a=a[::-1]
        return str(a[k-1])
            
        