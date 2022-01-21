from turtle import left


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashMap:
                return (hashMap[target-nums[i]], i)
            else:
                hashMap[nums[i]] = i


checker = Solution()
print(checker.twoSum(nums=[3,2,4], target=6))