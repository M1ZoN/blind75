class Solution:
    def updateMatrix(self, mat: int) -> int:
        x = len(mat)
        y = len(mat[x - 1])
        visited = []

        for i in range(x):
            for j in range(y):
                if mat[i][j] == 0:
                    visited.append((i, j))
                else:
                    mat[i][j] = "#"

        for i, j in visited:
            for addI, addJ in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                adjI = i + addI
                adjJ = j + addJ
            
                if 0 <= adjI < x and 0 <= adjJ < y and mat[adjI][adjJ] == "#":
                    mat[adjI][adjJ] = mat[i][j] + 1
                    visited.append((adjI, adjJ))
        
        return mat

