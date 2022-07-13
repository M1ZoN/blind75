# 13. Roman to Integer

```html 
Difficulty: <span style="color:green">**Easy**</span>.
```

# Description

Roman numerals are represented by seven different symbols: ```I```,```V```, ```X```, ```L```, ```C```, ```D``` and ```M```.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, ```2``` is written as ```II``` in Roman numeral, just two ones added together. ```12``` is written as ```XII```, which is simply ```X``` + ```II```. The number ```27``` is written as ```XXVII```, which is ```XX``` + ```V``` + ```II```.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not ```IIII```. Instead, the number four is written as ```IV```. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as ```IX```. There are six instances where subtraction is used:

```I``` can be placed before ```V``` (5) and ```X``` (10) to make 4 and 9. 
```X``` can be placed before ```L``` (50) and ```C``` (100) to make 40 and 90. 
```C``` can be placed before ```D``` (500) and ```M``` (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

# Solution

```python
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        intVal = 0
        hm = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X' : 10,'XL' : 40,'L' : 50,'XC' : 90,'C' : 100,'CD' : 400,'D' : 500,'CM' : 900,'M' : 1000}
        i = 0
        
        while i + 1 < len(s):
            if hm[s[i]] >= hm[s[i + 1]]:
                intVal += hm[s[i]]
                i += 1
            else:
                temp = "{}{}".format(s[i], s[i + 1])
                intVal += hm[temp]
                i += 2

        n = len(s) - 1
        if hm[s[n]] <= hm[s[n - 1]]:
            intVal += hm[s[n]]
        
        return intVal

a = Solution()
a.romanToInt("XLIVI")

# Or a soluting using only one hm and counting string:
class Solution:
    def romanToInt(self, s: str) -> int:
        a, r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200, "CM": -200}, 0
        for d, e in a.items():
            r += s.count(d) * e
        return r
```