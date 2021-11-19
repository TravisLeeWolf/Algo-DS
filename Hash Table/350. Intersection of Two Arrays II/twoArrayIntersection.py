class Solution:
    def intersect(self, nums1: "list[int]", nums2: "list[int]") -> "list[int]":
        intersection = []
        xCounter = 0
        yCounter = 0
    
        for x in range(len(nums1)):
            xCounter = x
            check = []
            for y in range(len(nums2)):
                yCounter = y
                while nums1[xCounter] == nums2[yCounter]:
                    check.append(nums1[xCounter])
                    if xCounter < len(nums1) - 1:
                        xCounter += 1
                    if yCounter < len(nums2):
                        yCounter += 1
                if len(check) > len(intersection) - 1:
                    intersection = check
                    

        return intersection

check = Solution()
print(check.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))