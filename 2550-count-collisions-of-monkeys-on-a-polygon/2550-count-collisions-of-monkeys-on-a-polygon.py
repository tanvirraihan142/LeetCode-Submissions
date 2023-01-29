class Solution:
    def monkeyMove(self, n: int) -> int:
        def myPow(x,n,m):
            p = 1
            if n<0:
                x = 1/x
                n = abs(n)
            while n:
                if n%2:
                    p*= x%m
                x*=x%m
                n//=2
            return p-2
        return myPow(2,n,(10**9+7)) % (10**9+7)