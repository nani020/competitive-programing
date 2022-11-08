class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        l= []
        ans = []
        for i in range(len(changed)):
            if l and l[0] * 2 == changed[i]:
                ans.append(heapq.heappop(l))
            else:
                heapq.heappush(l, changed[i]) 
        return ans if not l else []