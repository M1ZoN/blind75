# https://leetcode.com/problems/ransom-note/

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