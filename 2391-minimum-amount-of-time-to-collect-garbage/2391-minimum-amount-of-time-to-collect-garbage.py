class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ng = len(garbage)
        totaltime = 0
        for i in ["M", "P", "G"]:
            visit = False
            for j in range(ng-1, -1, -1):
                hg = garbage[j]
                picktime = hg.count(i)
                if picktime!=0:
                    visit = True
                if visit:
                    traveltime = 0 if j-1 < 0 else travel[j-1]
                    totaltime += picktime + traveltime
        return totaltime
