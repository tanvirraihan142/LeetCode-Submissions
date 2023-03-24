class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        q = collections.deque([0])
        visited = restricted
        count = 0
        
        while q:
            u = q.popleft()
            visited.add(u)
            count += 1
            for v in graph[u]:
                if v not in visited:
                    q.append(v)
                    
        return count
            