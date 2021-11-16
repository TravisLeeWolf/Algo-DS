class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashSet = set()
        answer = 0
        for number in nums:
            if (number not in hashSet):
                hashSet.add(number)
            else:
                hashSet.remove(number)
        answer = list(hashSet)
        return answer[0]

check = Solution()
print(check.singleNumber(nums=[4,1,2,1,2]))