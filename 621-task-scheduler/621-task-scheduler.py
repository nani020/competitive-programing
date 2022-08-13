class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = {}
        for i in tasks:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        l = sorted(x.values(), reverse = True)
        ma= l[0]
        
        i = 0
        counter = 0
        while i < len(l) and l[i] == ma:
            counter += 1
            i += 1
        
        ret = (ma - 1) * (n + 1) + counter
        return max(ret, len(tasks))