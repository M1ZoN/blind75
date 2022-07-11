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