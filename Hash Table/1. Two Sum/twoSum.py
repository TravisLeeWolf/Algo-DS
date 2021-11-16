class Solution:
    def twoSum(self, nums: "list[int]", target: int) -> "list[int]":
        hashmap = {}
        for i in range(len(nums)):
            hashmap[i] = nums[i]
        
        for x in hashmap:
            for y in hashmap:
                if (hashmap[x] + hashmap[y]) == target and x != y:
                    return [x, y]

check = Solution()
print(check.twoSum(nums=[3,2,4], target=6))
