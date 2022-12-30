class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        res = []
        
        q.append([0,[0]])
        
        while q:
            u, path = q.pop()

            if u == len(graph)-1:
                res.append(path)
                continue

            for v in graph[u]:
                q.append([v, path+[v]])

        return res