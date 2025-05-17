# Last updated: 5/17/2025, 5:58:18 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c in close_open_map:
                if stack and stack[-1] == close_open_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
