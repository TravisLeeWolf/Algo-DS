class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()
        for number in nums:
            if (number not in hashSet):
                hashSet.add(number)
            else:
                return True
        return False

check = Solution()
print(check.containsDuplicate(nums=[1,2,3,1]))