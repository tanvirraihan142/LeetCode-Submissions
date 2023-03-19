class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        
        def check_next_move(i,j,val):
          X = [2, 1, -1, -2, -2, -1, 1, 2]
          Y = [1, 2, 2, 1, -1, -2, -2, -1]

          for k in range(8):
            x = i + X[k]
            y = j + Y[k]

            if (0 <= x < len(grid) and 0 <= y < len(grid[0])):
              new_val = grid[x][y]
              if new_val == val+1:
                return [x,y]

          return [-1,-1]

        i,j,val = 0,0,0
        c = 1

        for k in range(len(grid)**2):
          i,j = check_next_move(i,j,val)
          # print(i,j,grid[i][j])
          if i==-1 and j==-1:
            break
          val = grid[i][j]
          c += 1

        if c==len(grid)**2:
          return True
        else:
          return False