# Last updated: 5/17/2025, 7:08:05 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            memo = [0 for i in range(n)]
            memo[0] = 1
            memo[1] = 2
            for i in range(2, len(memo)):
                memo[i] += memo[i-1]+memo[i-2]
            return memo[n-1]