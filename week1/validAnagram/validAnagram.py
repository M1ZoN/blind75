# https://leetcode.com/problems/valid-anagram/

def isAnagram(s, t):
    sDict = {}
    tDict = {}
    for i in s:
        if i in sDict:
            sDict[i] += 1
        else:
            sDict[i] = 1
    for i in t:
        if i in tDict:
            tDict[i] += 1
        else:
            tDict[i] = 1
    
    return sDict == tDict

def isAnagramTwo(s, t):
    for i in s:
        if i in t:
            t = t.replace(i, "", 1)
    return (t == "")

print(isAnagramTwo("anagram", "nagaram"))