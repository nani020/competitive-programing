class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        x=len(set(candyType))
        return min(x,len(candyType)//2)
        