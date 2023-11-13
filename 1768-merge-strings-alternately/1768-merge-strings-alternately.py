class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a= ""
        r= ""

        if len(word1) < len(word2):
            r = word2[len(word1):]
        elif len(word2) < len(word1):
            r= word1[len(word2):]
        
        for i in range(min(len(word1),len(word2))):
            a += word1[i]
            a += word2[i]
        a += r

        return a