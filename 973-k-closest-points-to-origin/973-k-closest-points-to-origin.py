class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_idx = []
        for idx,[x,y] in enumerate(points):
            distance_idx.append([(x**2+y**2),idx])
        distance_idx.sort()
        res = []
        for idx in range(k):
            op = distance_idx[idx][1]
            res.append(points[op])
        return res