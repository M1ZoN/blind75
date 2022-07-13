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