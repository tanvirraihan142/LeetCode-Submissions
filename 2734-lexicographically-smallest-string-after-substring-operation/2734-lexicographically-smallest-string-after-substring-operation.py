class Solution:
    def smallestString(self, s: str) -> str:
        list1 = s.split('a')
        # print(list1)
        idx = 0
        for i in range(len(list1)):
            if len(list1[i])>0:
                idx = i
                break
        op = 0
        a = list(list1[idx]) 
        for i in range(len(a)):
            a[i] = chr(ord(a[i])-1)
            op = 1
            
        list1[idx] = "".join(a)
        s2 = "a".join(list1)
        if op == 0:
            s2 = s2[:-1] + 'z'
        return s2