class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if (len(stones) == 1):
            return 0
        
        max_path = 0
        mapper = {}
        
        visited = set()
        
        for i in range(len(stones)):
            starter = stones[i]
            
            queue = deque()
            queue.appendleft([starter[0],starter[1],0])
            
            visited.add(i)
            
            while queue:
                #print(queue)
                x,y,s = queue.popleft()             
                for j in range(len(stones)):
                    
                    if stones[j][1] == y and stones[j][0] != x and j not in visited:
                        #max_path = max(max_path,s+1)
                        max_path += 1
                        queue.appendleft([stones[j][0],y,s+1])
                        visited.add(j)
                        
                    if stones[j][0] == x and stones[j][1] != y and j not in visited:
                        #max_path = max(max_path,s+1)
                        max_path += 1
                        queue.appendleft([x,stones[j][1],s+1])
                        visited.add(j)
                        
            #print(visited)
            
            
        return max_path