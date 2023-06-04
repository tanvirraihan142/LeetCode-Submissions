class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def f(size, digit_sum):
            @cache
            def dp(i, curr, lower):
                if curr > digit_sum:
                    return 0
                if i == len(size):
                    return 1
                
                ans = 0
                if lower:
                    for num in range(10):
                        ans += dp(i + 1, curr + num, lower)
                else:
                    for num in range(1 + int(size[i])):
                        ans += dp(i + 1, curr + num, num < int(size[i]))
                        
                return ans % MOD
            
            size = str(size)
            return dp(0, 0, False)
        
        MOD = 10 ** 9 + 7
        num1 = int(num1)
        num2 = int(num2)
        return (f(num2, max_sum) - f(num1 - 1, max_sum) - f(num2, min_sum - 1) + f(num1 - 1, min_sum - 1)) % MOD