class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        myMax = 0
        sz = len(s)

        i = 0
        j = i
        while i < sz and j < sz:
            if s[j] in hm:
                hm = {}
                myMax = max(myMax, j - i)
                i += 1
                j = i
            else:
                hm[s[j]] = 1
                j += 1

        myMax = max(myMax, j - i)
        return myMax 