# Last updated: 4/23/2025, 5:41:51 PM
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        visited = set()
        i = 0
        score = 0

        while 0 <= i < n and i not in visited:
            visited.add(i)

            if instructions[i] == "add":
                score += values[i]
                i += 1
            elif instructions[i] == "jump":
                i += values[i]

        return score