class Solution:
    def minimumCardPickup(self, cards: List[int])-> int:
        seen={}
        best=10** 20
        N =len(cards)
        for i, c in enumerate(cards):
            if c in seen:
                best=min(best, i - seen[c] +1)
            seen[c]=i
        if best==10 ** 20:
            return -1
        return best