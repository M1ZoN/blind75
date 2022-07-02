# https://leetcode.com/problems/valid-palindrome/submissions/

def isPalindrome(s):
    trimmed = ''.join(filter(str.isalnum, s)).lower()
    revTrim = trimmed[::-1]

    return trimmed == revTrim

print(isPalindrome("A man, a plan, a canal: Panama"))
