# 242. Valid Anagram

Date Created: July 1, 2022 5:28 PM
Difficulty: Easy
Due Date: July 4, 2022
Status: Completed
Week #: Week 1

# Description

Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of* `s`*, and* `false` *otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true

```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```

# Solution

```python
def isAnagram(s, t): #Faster solution
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
```