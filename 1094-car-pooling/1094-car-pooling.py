class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        p= 0
        for loc in lst:
            p += loc[1]
            if p > capacity:
                return False
        return True