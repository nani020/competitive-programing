class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        x = []
        for i in intervals:
            if not x or x[-1][1] < i[0]:
                x.append(i)
            else:
                x[-1][1] = max(x[-1][1], i[1])
        return x
   