class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = defaultdict(set)

        # Add the edges to the adjacency list
        for i, j in edges:
            adjacency_list[i-1].add(j-1)
            adjacency_list[j-1].add(i-1)



        degrees = [0] * (n)
        for a, b in edges:
            degrees[a-1] += 1
            degrees[b-1] += 1

        odd_count = 0
        odd_vertices = []

        for i, degree in enumerate(degrees):
            if degree % 2 == 1:
                odd_count += 1
                odd_vertices.append(i)

        if odd_count == 0:
            return True

        elif odd_count == 2:
            a = odd_vertices[0]
            b = odd_vertices[1]
            for k in range(n):
                if k not in adjacency_list[a] and k not in adjacency_list[b]:
                    return True
            return False

        elif odd_count==4:
            a = odd_vertices[0]
            b = odd_vertices[1]
            c = odd_vertices[2]
            d = odd_vertices[3]

            if b not in adjacency_list[a] and d not in adjacency_list[c] or c not in adjacency_list[a] and d not in adjacency_list[b] or d not in adjacency_list[a] and c not in adjacency_list[b]:
                return True
            return False
        else:
            return False