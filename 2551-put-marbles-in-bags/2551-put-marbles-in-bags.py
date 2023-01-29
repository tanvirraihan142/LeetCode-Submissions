class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        v, d = [0] * (len(weights) - 1), 0
        for i in range(len(weights) - 1):
            v[i] = weights[i] + weights[i + 1]
        v.sort()
        for i in range(k - 1):
            d += v[len(weights) - 2 - i] - v[i]
        return d