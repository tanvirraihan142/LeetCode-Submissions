class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        def f(x):
            c = collections.Counter(x)
            r = 1
            a = 1
            for l in sorted(c.values(), reverse=True):
                for i in range(1, l + 1):
                    r = r * a // i
                    a += 1
            return r % MOD           

        ret = 1
        for w in s.split(' '):
            ret = (ret * f(w)) % MOD
            
        return ret