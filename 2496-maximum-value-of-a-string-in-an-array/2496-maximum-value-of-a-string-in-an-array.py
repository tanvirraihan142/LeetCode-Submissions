class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        values = []
        for i in strs:
            if i.isalpha():
                values.append(len(i))
                # print(i,"yes")
            elif i.isdigit():
                values.append(int(i))
                # print(i,"no")
            else:
                values.append(len(i))
        return max(values)