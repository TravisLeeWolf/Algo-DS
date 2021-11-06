
def lengthOfLongestSubstring(s: str) -> int:
        rightSide = 0
        substring = []
        maxLength = 0

        while rightSide < len(s):
            while s[rightSide] in substring:
                del substring[0]
            
            substring.append(s[rightSide])
            rightSide += 1
            
            if len(substring) >= maxLength:
                maxLength = len(substring)
            
        
        return maxLength

print(lengthOfLongestSubstring(s="abcabcbb"))


