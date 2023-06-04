class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows, cols = n, n
        visited_rows = set()
        visited_cols = set()
        result = 0
        while queries:
            t, i, v = queries.pop()
            if t == 0 and i not in visited_rows: # row operation
                result += v*cols
                rows -= 1
                visited_rows.add(i)
            elif t == 1 and i not in visited_cols:
                result += v*rows
                cols -= 1
                visited_cols.add(i)
 
        return result