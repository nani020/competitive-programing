class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfdivi(number):
            for i in str(number):
                if i=='0' or int(number)%int(i)!=0:
                    return False
            return True
        l=[]
        for i in range(left,right+1):
            if selfdivi(i):
                l.append(i)
        return l        
        
        