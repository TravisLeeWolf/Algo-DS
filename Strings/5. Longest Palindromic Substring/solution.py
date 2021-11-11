class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        palidrome = []
        positionA = 0
        positionB = 0
        step = 1

        while positionA < len(s):
            possiblePalindrome = [s[positionA]]
            if positionA != 0:
                try:
                    while s[positionA - step] == s[positionA + step]:
                        possiblePalindrome.append(s[positionA + step])
                        possiblePalindrome.insert(0, s[positionA - step])
                        step += 1
                    step = 1
                    if possiblePalindrome > palidrome:
                        palidrome = possiblePalindrome
                    positionA += 1
                except IndexError:
                    break
            else:
                positionA += 1

        solution = "".join(palidrome)
        
        return solution



palidrome = LongestPalindrome()
print(palidrome.longestPalindrome(s="babad"))