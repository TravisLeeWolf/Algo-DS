class Solution:
    def firstUniqChar(self, s: str) -> int:
        occuranceMap = {}
        for letter in s:
            if letter not in occuranceMap.keys():
                occuranceMap[letter] = 1
            else:
                occuranceMap[letter] += 1


        for key in occuranceMap:
            if occuranceMap[key] == 1:
                return s.index(key)
        return -1

check = Solution()
print(check.firstUniqChar(s="aabb"))