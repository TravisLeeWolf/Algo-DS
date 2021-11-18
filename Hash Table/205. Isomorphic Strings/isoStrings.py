class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isoMap = {}
        for i in range(len(s)):
            if s[i] not in isoMap.keys():
                if t[i] in isoMap.values():
                    return False
                else:
                    isoMap[s[i]] = t[i]
            elif isoMap[s[i]] != t[i]:
                return False
            i += 1
        return True

check = Solution()
print(check.isIsomorphic(s="badc", t="baba"))