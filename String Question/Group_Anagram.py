# Group anagram 
# Creating the default dict list of the string 
from collections import defaultdict


def group_anagram(string):
    group = defaultdict(list)
    def generate_key(string):
        chars = [0]*27 
        for s in string:
            num = ord(s)-ord('a')
            chars[num] += 1
       
        return "_".join([str(i)+str(chars[i]) for i in range(27) if chars[i]])

    for s in string:
        key = generate_key(s)
        group[key].append(s)
    return group.values()
string = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(string))