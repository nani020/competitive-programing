
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stri = list()
        for n in num:
            while stri and k and stri[-1] > n:
                stri.pop()
                k -= 1
            if stri or n is not '0':
                stri.append(n)
        if k: 
            stri = stri[0:-k]
        return ''.join(stri) or '0'