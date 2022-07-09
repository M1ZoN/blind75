# 383. Ransom Note

Date Created: July 6, 2022 5:47 PM
Difficulty: Easy
Due Date: July 11, 2022
Status: Next Up
Week #: Week 2

# Description

Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**

```
Input: ransomNote = "a", magazine = "b"
Output: false

```

**Example 2:**

```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

**Example 3:**

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

# Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_m = {}
        
        for i in magazine:
            if i in hash_m:
                hash_m[i] += 1
            else:
                hash_m[i] = 1

        for i in ransomNote:
            if i not in hash_m:
                return False
            if hash_m[i] == 1:
                hash_m.pop(i)
            else:
                hash_m[i] -= 1

        return True

print(Solution().canConstruct("aa", "ab"))
```