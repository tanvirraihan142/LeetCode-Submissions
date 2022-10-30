class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digitsum(x):
            _sum = 0
            while x > 0:
                _sum += (x%10)
                x //= 10
            return _sum
        
        n2 = n
        ans = 0
        i = 1
        while True:
            if digitsum(n) <= target:
                break 

            n = ((n//(10**i))+1)*(10**i)
            i += 1
            # print(n)
            ans = n - n2
        return ans