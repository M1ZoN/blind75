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
print(isValid("{}()[]"))