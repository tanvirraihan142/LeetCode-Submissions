class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        painted_rows, painted_cols = set(), set()
        _map = {}

        m_c = [0 for i in range(n)]
        n_c = [0 for i in range(m)]

        for i in range(m):
            for j in range(n):
                _map[mat[i][j]] = (i,j)
                mat[i][j] = 0


        for i,num in enumerate(arr):
            row, col = _map[num]
            m_c[col] += 1
            n_c[row] += 1

            if m_c[col] == m or n_c[row] == n:
                return i