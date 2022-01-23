class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # For the case of 1
        if numRows == 1:
            return [[1]]

        # Working out Pascals triangle
        pascalsTri = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(pascalsTri[i-1][j-1] + pascalsTri[i-1][j])
            row.append(1)
            pascalsTri.append(row)

        return pascalsTri