class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        n = len(skill)
        skill.sort()
        for i in range(int(n/2)):
            if (skill[i] + skill[n-1-i]) != (skill[0] + skill[n-1]):
                return -1
            
            ans += skill[i] * skill[n-1-i]
            
        return ans