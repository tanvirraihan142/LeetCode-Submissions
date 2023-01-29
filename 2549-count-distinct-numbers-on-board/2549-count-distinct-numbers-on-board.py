class Solution:
    def distinctIntegers(self, n: int) -> int:
        distinct_numbers = set([n])
        for day in range(109):
            new_numbers = set()
            for x in distinct_numbers:
                for i in range(1, n+1):
                    if x % i == 1:
                        new_numbers.add(i)
            distinct_numbers = distinct_numbers.union(new_numbers)
        return len(distinct_numbers)