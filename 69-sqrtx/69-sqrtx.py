class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, x + 1):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1
            
        return -1
       