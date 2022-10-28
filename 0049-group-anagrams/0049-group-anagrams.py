class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = [strs[i] for i in range(len(strs))]
        for i in range(len(a)):
            a[i] = list(a[i])
            a[i].sort()
            a[i] = "".join(a[i])
        hasher = {}
        for i in range(len(a)):
            if a[i] not in hasher:
                hasher[a[i]] = [i]
            else:
                hasher[a[i]].append(i)

        result = [[] for i in hasher]
        k = 0
        for i in hasher:
            for j in hasher[i]:
                result[k].append(strs[j])
            k += 1
        return result 