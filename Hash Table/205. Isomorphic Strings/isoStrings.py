class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stringMapS = {}
        for i in range(len(s)):
            if s[i] not in stringMapS.keys():
                stringMapS[s[i]] = i
            else:
                stringMapS[s[i]] = [stringMapS[s[i]], i]

        stringMapT = {}
        for i in range(len(t)):
            if t[i] not in stringMapT.keys():
                stringMapT[t[i]] = i
            else:
                stringMapT[t[i]] = [stringMapT[t[i]], i]

        changedMap = dict(zip(stringMapT.keys(), list(stringMapS.values())))

        newString = []
        for _ in range(len(s)):
            newString.append("0")
        
        for key in changedMap:
            try:
                for index in changedMap[key]:
                    newString[index] = key
            except:
                newString[changedMap[key]] = key

        newString = ''.join(newString)


        return newString == t






check = Solution()
print(check.isIsomorphic(s="aaeaa", t="uuxyy"))