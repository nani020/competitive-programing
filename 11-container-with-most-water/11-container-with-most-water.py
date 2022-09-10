class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        f=0
        l=len(height) - 1
        while f < l:
            area= ((l - f) * min(height[f], height[l]))
            maxi= max(area,maxi)
            if height[f] >=  height[l]:
                l-= 1
            else:
                f += 1
        return maxi 