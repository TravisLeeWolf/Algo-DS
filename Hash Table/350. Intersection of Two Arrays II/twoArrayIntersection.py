class Solution:
    def intersect(self, nums1: "list[int]", nums2: "list[int]") -> "list[int]":
        intersection = []
        nums1.sort()
        nums2.sort()
    
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            elif nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
                    

        return intersection

check = Solution()
print(check.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))