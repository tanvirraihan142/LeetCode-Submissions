class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        a = nums
        n = len(a)
        r = sum(a)
        for i in range(1, n):
            a = [min(a[j], a[j-1]) for j in range(n)]
            r = min(r, sum(a) + x * i)
        return r