class Solution:
    def minScore(self, n: int, road: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(road)):
            graph[road[i][0]].append([road[i][1], road[i][2]])
            graph[road[i][1]].append([road[i][0], road[i][2]])
          
        
        road.sort(key= lambda x:x[2])
        
        def isReachable(s, d):
            nonlocal n
            visited = set()

            # Create a queue for BFS
            queue=collections.deque([])

            # Mark the source node as visited and enqueue it
            queue.append(s)
            visited.add(s)

            while queue:

                #Dequeue a vertex from queue
                u = queue.popleft()

                # If this adjacent node is the destination node,
                # then return true
                if u == d:
                    return True

                #  Else, continue to do BFS
                for v,w in graph[u]:
                    if v not in visited:
                        queue.append(v)
                        visited.add(v)
             # If BFS is complete without visited d
            return False
        
        
        
        
        min_cost = float('inf')
        for u,v,w in road:
            if isReachable(1, u) or isReachable(1, v):
                min_cost = min(min_cost, w)
            if w > min_cost:
                break
                
        return min_cost