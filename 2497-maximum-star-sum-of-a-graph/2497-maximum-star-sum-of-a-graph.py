class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if k==0:
            return max(vals)
        
        if len(edges)==0:
            return max(vals)
        
        # Build a map from node to its value
        node_values = {i: v for i, v in enumerate(vals)}

        # Build a map from node to its neighbors
        neighbors = collections.defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # Compute all possible star graphs with at most k edges
        max_star_sum = 0
        for center, neighbor_set in neighbors.items():
            neighbor_set.sort(key=lambda x:-node_values[x])

        max_star_sum = 0
        for center, neighbor_set in neighbors.items():
            neighbor_set2 = neighbor_set[:k]
            star_sum = node_values[center]
            for v in neighbor_set2:
                star_sum = max(star_sum, star_sum + node_values[v])
            max_star_sum = max(max_star_sum, star_sum)
            
        return max_star_sum