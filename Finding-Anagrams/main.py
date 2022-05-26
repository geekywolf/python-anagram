# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from cgi import test


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # check if both words are the same length
    if len(word) == len(anagram):
        # Sort words in ascending order and compare values
        if(sorted(word) == sorted(anagram)):
           return print("Both strings form an Anagram.")
        else:
            return print("Both strings do not form an Anagram.")
    else:
        return print("Both strings do not form an Anagram.")

test1 = str(input("Enter a word:    "))
test2 = str(input("Enter another word:    "))

find_anagram(test1, test2)