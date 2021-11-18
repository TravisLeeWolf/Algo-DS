class Solution:
    def intersect(self, nums1: "list[int]", nums2: "list[int]") -> "list[int]":
        intersect = []
        if len(nums1) > len(nums2):
            longNumber = nums1
            shortNumber = nums2
        else:
            longNumber = nums2
            shortNumber = nums1
        
        for x in longNumber:
            for y in shortNumber:
                if y == x:
                    intersect.append(y)

        return intersect

check = Solution()
print(check.intersect(nums1=[1,2,2,1], nums2=[2,2]))