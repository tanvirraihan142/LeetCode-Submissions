class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key = lambda x:x[0])
        
        for i in range(len(intervals)):
            if not stack:
                stack.append(intervals[i])
                
            else:
                recent = stack[-1]
                previous_end = recent[1]
                current_start = intervals[i][0]
                
                if current_start <= previous_end:
                    stack.pop()
                    stack.append([recent[0], max(recent[1], intervals[i][1])])
                else:
                    stack.append(intervals[i])
                    
        return stack