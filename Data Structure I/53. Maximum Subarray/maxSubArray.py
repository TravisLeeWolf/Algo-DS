from operator import le
import re


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        subArraySum = 0
        maxSum = nums[0]

        for number in nums:
            subArraySum += number
            if subArraySum < number:
                subArraySum = number
            if maxSum < subArraySum:
                maxSum = subArraySum

        return maxSum


checker = Solution()
print(checker.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))