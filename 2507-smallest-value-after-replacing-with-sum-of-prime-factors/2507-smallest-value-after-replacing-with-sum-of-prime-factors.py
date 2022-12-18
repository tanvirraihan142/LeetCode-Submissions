class Solution:
    def smallestValue(self, n: int) -> int:
        def primeFactors(n):
            _arr = []
            while n%2 == 0:
                _arr.append(2)
                n = n/2
            for i in range(3,int(math.sqrt(n))+1,2):
                while n % i== 0:
                    _arr.append(i)
                    n = n/i
            if n>2:
                _arr.append(int(n))
            return sum(_arr)


        def sieve_of_eratosthenes(n):
            # Create a boolean array "prime[0..n]" and 
            # initialize all entries it as true.
            prime = [True for _ in range(n+1)]
            p = 2
            while p * p <= n:
                # If prime[p] is not changed, then it is a prime
                if prime[p]:
                    # Update all multiples of p
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1

            return prime


        prime = sieve_of_eratosthenes(10**5)
        _min = float('inf')
        n2 = n
        if prime[n2] or n2==4:
            return n2

        while prime[n2] == False:
            n2 = primeFactors(n2)
            # print(n2, _min)
            _min = min(_min, n2)

        return _min