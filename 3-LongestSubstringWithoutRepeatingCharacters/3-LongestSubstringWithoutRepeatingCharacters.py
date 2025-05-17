# Last updated: 5/17/2025, 5:55:44 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in set(['(','{','[']):
                stack.append(c)
            else:
                if len(stack)>0 and ((c==']' and stack[-1]=='[') or \
                 (c==')' and stack[-1] == '(') or \
                  (c=='}' and stack[-1]=='{')):
                    stack.pop()
                else:
                    return False
        if not stack:        
            return True
        else:
            return False