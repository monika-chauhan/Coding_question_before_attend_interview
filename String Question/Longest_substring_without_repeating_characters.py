# using Sliding Window and Two Pointer 
def Longest_substring_without_repeating_char(s):
    length = left = 0
    count = {}
    right = 0 
    while right < len(s):
        count[s[right]] = 1 + count.get(s[right], 0)
        while count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1
        length = max(length, right - left + 1)
     
        right += 1
    return length

s1= ""
s2=" "
s3 = "abcabacd"
print(Longest_substring_without_repeating_char(s1))
print(Longest_substring_without_repeating_char(s2))
print(Longest_substring_without_repeating_char(s3))

    
