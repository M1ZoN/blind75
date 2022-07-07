# Valid Parentheses

Date Created: July 1, 2022 5:08 PM
Difficulty: Easy
Due Date: July 1, 2022
Status: Completed
Week #: Week 1

# Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false
```

# Solution

Interesting solution, but slow:

```python
def isValid(str):
	  if len(s) % 2 != 0:
            return False

    while (len(s) > 0):
        if '()' in s:
            s = s.replace("()", "")
        elif '[]' in s:
            s = s.replace("[]", "")
        elif '{}' in s:
            s = s.replace("{}", "")
        else:
            return False

    if len(s) == 0:
        return True

```

Stack:

```python
def isValid(s):
    stack = []
    openBracket = {"{", "(", "["}
    closeBracket = {"}", ")", "]"}
    pair = {"{":"}", "(":")", "[":"]"}
    valid = True
    i = 0

    while i < len(s) and valid:
        if s[i] in openBracket:
            stack.append(s[i])
        elif s[i] in closeBracket and stack:
            if pair[stack[-1]] == s[i]:
                stack.pop()
            else:
                valid = False
        else:
            valid = False
        i += 1
    return not stack and valid

print(isValid("(]"))
```