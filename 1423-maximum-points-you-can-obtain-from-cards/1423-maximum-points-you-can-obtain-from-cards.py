class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curt= len(cardPoints)-k
        c = sum(cardPoints[curt:])
        index = 0
        ans = c
        while curt<len(cardPoints):
            c = c - cardPoints[curt] + cardPoints[index]
            ans = max(ans, c)
            curt+=1
            index+=1
        return ans
    
    
        # it is k sized sliding window
        # the time complexity is O(n) and the space complexity could be O(1)