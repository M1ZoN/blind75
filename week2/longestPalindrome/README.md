# 409. Longest Palindrome

Date Created: July 6, 2022 5:49 PM
Difficulty: Easy
Due Date: July 12, 2022
Status: Next Up
Week #: Week 2

# Description

Given a string `s` which consists of lowercase or uppercase letters, return *the length of the **longest palindrome*** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome here.

**Example 1:**

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

```

**Example 2:**

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

```

# Solution

```python
# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        count = 0

        for i in s:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
                
        for i in hm:
            if hm[i] % 2 == 0:
                count += hm[i]
            else:
                if hm[i] > 1:
                    count += hm[i] - 1
                    hm[i] = 1
                    
        for i in hm:
            if hm[i] % 2 == 1:
                return count + 1

        return count

Solution().longestPalindrome("abccccdd")
```