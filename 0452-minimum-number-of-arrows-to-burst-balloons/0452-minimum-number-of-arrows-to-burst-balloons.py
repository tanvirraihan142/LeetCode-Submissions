class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)
        prevEnd = points[0][1]
        
        for start, end in points[1:]:
            if start > prevEnd:
                prevEnd = end
            else:
                res -= 1
                prevEnd = min(prevEnd, end)
                
        return res