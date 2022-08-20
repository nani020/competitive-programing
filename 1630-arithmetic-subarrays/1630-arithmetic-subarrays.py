class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arth=[]
        for i in range(len(l)):
            x=sorted(nums[l[i]:r[i]+1])
            count=1
            diff=x[1]-x[0]
        
            for j in range(1, len(x)):
                if x[j] - x[j-1] != diff:
                        arth.append(False)
                        count = 0
                        break

            if count==1:
                arth.append(True)
            
        return arth
