class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Create topLeft and bottomRight arrays
        topLeft = [[set() for _ in range(n)] for _ in range(m)]
        bottomRight = [[set() for _ in range(n)] for _ in range(m)]

        # Calculate topLeft and bottomRight
        for r in range(1,m):
            for c in range(1,n):
                topLeft[r][c] = topLeft[r-1][c-1].copy()
                topLeft[r][c].add(grid[r-1][c-1])


        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                bottomRight[r][c] = bottomRight[r+1][c+1].copy()
                bottomRight[r][c].add(grid[r+1][c+1])

        # Create answer matrix
        answer = [[0] * n for _ in range(m)]

        # Calculate answer
        for r in range(m):
            for c in range(n):
                answer[r][c] = abs(len(topLeft[r][c]) - len(bottomRight[r][c]))

        return answer