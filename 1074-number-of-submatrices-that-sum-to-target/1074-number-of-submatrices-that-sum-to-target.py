class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m= len(matrix)
        n=len(matrix[0])
        res=0
        for row in matrix:
            for i in range(1,len(row)):
                row[i] += row[i-1]
        for i in range(n):
            for j in range(i, n):
                c = defaultdict(int)
                cur=0
                c[0] =1
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res
        
        
        