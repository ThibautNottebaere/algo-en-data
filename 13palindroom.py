def isPalindroom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[len(s) - 1]:
        return False
    return isPalindroom(s[1:len(s) - 1])
