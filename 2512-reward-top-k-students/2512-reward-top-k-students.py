class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        points = {}
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        
        for i in range(len(report)):
            words = report[i].split()
            points[student_id[i]] = 0
            
            for word in words:
                if word in positive_feedback:
                    points[student_id[i]] += 3
                elif word in negative_feedback:
                    points[student_id[i]] -= 1
        
        sorted_students = sorted(points, key=lambda x: (-points[x], x))
        return sorted_students[:k]