# using two pointers 
# Approach :

def Longest_Palindrome_substring(s):
    if not s:
        return ''
    res = ''
    for i in range(len(s)):
        p1 = isPalindrome(s,i,i)
        p2 = isPalindrome(s,i,i+1)
        if len(res) < len(p1):
            res = p1 
        if len(res) < len(p2):
            res = p2 
    return res 

def isPalindrome(s,i,j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]

string = "babad"
print(Longest_Palindrome_substring(string))