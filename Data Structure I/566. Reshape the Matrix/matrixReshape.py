class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # If reshape is not legal
        if len(mat) * len(mat[0]) != r * c:
            return mat

        # Reshape matrix
        answer = [[]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                value = mat[i][j]
                if len(answer[-1]) < c:
                    answer[-1].append(value)
                else:
                    answer.append([value])
        
        return answer