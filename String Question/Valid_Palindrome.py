# Using Slicing in Python 
string = "madam"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Two Pointer Approach 
def isPalindrome(string):
    start = 0 
    end = len(string) - 1
    while start <= end:
        if string[start] != string[end]:
            return False 
        start += 1
        end -= 1
    return True 

string = 'madam'
print(isPalindrome(string))
second_string = 'Palindrome'
print(isPalindrome(second_string))
