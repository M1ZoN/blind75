# 542. 01 Matrix

Difficulty: ![#F4D50A](https://via.placeholder.com/16/F4D50A/F4D50A.png) Medium

```https://leetcode.com/problems/01-matrix/```

# Description

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

**Example 1:**

![image1](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

**Example 2:**

![image2](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

# Solution

```python
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
```