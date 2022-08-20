class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort();
        x=len(piles)
        
        you = 0;
        for i in range(x//3):
            you += piles[x-2-2*i];
        return you;