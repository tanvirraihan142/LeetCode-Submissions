class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x)

        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                roads = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    roads -= 1
                result = max(result, roads)
        return result