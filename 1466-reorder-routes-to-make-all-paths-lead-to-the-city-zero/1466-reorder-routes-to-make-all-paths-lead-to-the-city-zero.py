class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        count = 0
        
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        given_edges = set([(u,v) for u,v in connections])
        
        q = collections.deque()
        q.append(0)
        
        while len(q)>0:
            u = q.popleft()
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    q.append(v)
                    if (u,v)  in given_edges:
                        count += 1
                    
        return count
        
            