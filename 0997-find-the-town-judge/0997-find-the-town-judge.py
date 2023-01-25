class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjacency_list = dict()
        adjacency_list_2  = dict()
        
        for i in range(1,n+1):
            adjacency_list[i] = []
            adjacency_list_2[i] = []
            
        for edge in trust:
            from_node = edge[0]
            to_node = edge[1]
            adjacency_list[from_node].append(to_node)
            adjacency_list_2[to_node].append(from_node)
            
        town_judge_node = -1
        
        for item in adjacency_list.items():
            if len(item[1])==0:
                if len(adjacency_list_2[item[0]])==(n-1):
                    town_judge_node = item[0]
                    
                
        return town_judge_node