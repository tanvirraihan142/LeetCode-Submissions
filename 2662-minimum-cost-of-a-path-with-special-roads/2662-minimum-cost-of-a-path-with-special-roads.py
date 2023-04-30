class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        v, d, q = collections.defaultdict(list), collections.defaultdict(int), set()
        for x in specialRoads:
            v[(x[0], x[1])].append([x[2], x[3], min(x[4], abs(x[0] - x[2]) + abs(x[1] - x[3]))])
            v[(start[0], start[1])].append([x[0], x[1], abs(x[0] - start[0]) + abs(x[1] - start[1])])
            v[(x[2], x[3])].append([target[0], target[1], abs(x[2] - target[0]) + abs(x[3] - target[1])])
            for y in specialRoads:
                v[(x[2], x[3])].append([y[0], y[1], abs(x[2] - y[0]) + abs(x[3] - y[1])])
        v[(start[0], start[1])].append([target[0], target[1], abs(target[0] - start[0]) + abs(target[1] - start[1])])
        q.add((0, start[0], start[1]))
        while q:
            c = list(q)[0]
            q.remove(c)
            for x in v[c[1], c[2]]:
                if not (x[0], x[1]) in d or d[(c[1], c[2])] + x[2] < d[(x[0], x[1])]:
                    if (d[(x[0], x[1])], x[0], x[1]) in q:
                        q.remove((d[(x[0], x[1])], x[0], x[1]))
                    d[(x[0], x[1])] = d[(c[1], c[2])] + x[2]
                    q.add((d[(x[0], x[1])], x[0], x[1]))
        return d[(target[0], target[1])]