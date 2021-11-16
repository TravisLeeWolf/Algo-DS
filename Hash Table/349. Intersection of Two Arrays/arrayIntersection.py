class Solution:
    def intersection(self, nums1: "list[int]", nums2: "list[int]") -> "list[int]":
        intersection = set()
        for x in nums1:
            if x in nums2:
                intersection.add(x)
        answer = []
        for y in intersection:
            answer.append(y)

        return(answer)





nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
check = Solution()
print(check.intersection(nums1, nums2))