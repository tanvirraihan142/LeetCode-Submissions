class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1

            primes = []
            for num in range(2, n + 1):
                if is_prime[num]:
                    primes.append(num)

            return primes

        primes = sieve_of_eratosthenes(n)
        _set = set(primes)
        result = []
        for i in range(len(primes)):
          if n-primes[i] in _set and primes[i] <= n//2:
            result.append([primes[i], n-primes[i]])
        return result