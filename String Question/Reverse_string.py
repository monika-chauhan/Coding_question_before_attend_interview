# Simple Approach using slicing  in python 
string = 'Welcome'
print(string[::-1])

# using Two Pointer Approach 
def reverse_string(string):
    string_list = string.split( )
    start = 0 
    end = len(string_list) - 1
    while start <= end:
        string_list[start],string_list[end] = string_list[end],string_list[start]
        start += 1
        end -= 1
    return ' '.join(string_list)

string = "Welcome To Python World"
print(reverse_string(string))