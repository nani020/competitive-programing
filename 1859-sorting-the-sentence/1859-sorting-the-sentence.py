class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(s.split())
        res=[0]*len(s)
        for word in s:
            res[int(word[-1])-1]=word[:-1]
        return" ".join(res)    
        