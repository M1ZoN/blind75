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