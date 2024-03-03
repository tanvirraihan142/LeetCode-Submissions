class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2
        diff_count = 0
        same_count = 0
        count = defaultdict(int)
        # Iterate through each cell of the grid
        y_cells = set()


        for i in range(n//2+1):
          count[grid[i][i]] += 1
          count[grid[i][n-1-i]] += 1
          y_cells.add((i,i))
          y_cells.add((i,n-1-i))


        count[grid[n//2 ][n//2 ]] -= 1


        for i in range(n//2+1, n):
          count[grid[i][n//2]] += 1
          y_cells.add((i,n//2))


        count2 = defaultdict(int)

        for i in range(n):
          for j in range(len(grid[0])):
            if (i,j) in y_cells:
              continue
            else:
              count2[grid[i][j]] += 1

        return min(#zero + one
            count[1]+count[2] + count2[0]+count2[2],
            #zero + two
            count[1]+count[2] + count2[0]+count2[1],
            #one + zero
            count[0]+count[2] + count2[1]+count2[2],
            #one + two
            count[0]+count[2] + count2[1]+count2[0],
            #two + one
            count[1]+count[0] + count2[0]+count2[2],
            #two + zero
            count[1]+count[0] + count2[1]+count2[2],
            )