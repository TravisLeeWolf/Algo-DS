from typing import Counter


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            numbers = str(n)
            array = []
            for num in numbers:
                power = int(num) ** 2
                array.append(power)
            n = sum(array)
            return n

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


check = Solution()
print(check.isHappy(n=19))