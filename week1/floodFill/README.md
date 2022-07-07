# 733. Flood Fill

Date Created: July 2, 2022 10:05 AM
Difficulty: Easy
Due Date: July 5, 2022
Status: Completed
Week #: Week 1

# Description

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `color`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.

Return *the modified image after performing the flood fill*.

![Untitled](733%20Flood%20Fill%20712d99d8a98e49a5b9629e3c8c1f9b39/Untitled.png)

**Example 1:**

```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

```

**Example 2:**

```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
```

# Solution

```python
#  https://leetcode.com/problems/flood-fill/

def floodFill(image, sr, sc, color):

    i = 0
    j = 0
    if (image[sr][sc] == color):
        return image

    visited = []
    prevColor = image[sr][sc]
    image[sr][sc] = color
    while i < len(image):
        while j < len(image[i]):
            if image[i][j] == prevColor and ((i - 1 == sr or i + 1 == sr) and j == sc or (j - 1 == sc or j + 1 == sc) and i == sr):
                visited.append([i,j])
                image[i][j] = color
                i = 0
                j = 0
                continue
            if image[i][j] == prevColor and ( i - 1 >= 0 and [i - 1, j] in visited or (i + 1 < len(image)) and [i + 1, j] in visited or (j - 1 >= 0) and [i, j - 1] in visited or (j + 1 < len(image[i])) and [i, j + 1] in visited):
                visited.append([i,j])
                image[i][j] = color
                i = 0
                j = 0
                continue
            j += 1
        i += 1
        j = 0    

    i = 0
    j = 0

    while i < len(image):
        while j < len(image[i]):            
            print(image[i][j], end=" ")
            j += 1
        print()
        i += 1
        j = 0

floodFill([[0,1,0],[0,0,1]], 1, 1, 1)
```