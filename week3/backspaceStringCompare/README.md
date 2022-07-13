# 844. Backspace String Compare

Difficulty: ![#D9F8C4](https://via.placeholder.com/15/D9F8C4/D9F8C4.png) Easy

# Description

Given two strings ```s``` and ```t```, return ```true``` *if they are equal when both are typed into empty text editors*. ```'#'``` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac"
```

**Example 2:**

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```

**Example 3:**

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

# Solution

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arrS = []
        arrT = []

        for i in s:
            if i != '#':
                arrS.append(i)
            else:
                if arrS:
                    arrS.pop()
        
        for i in t:
            if i != '#':
                arrT.append(i)
            else:
                if arrT:
                    arrT.pop()
        
        return arrS == arrT
```
