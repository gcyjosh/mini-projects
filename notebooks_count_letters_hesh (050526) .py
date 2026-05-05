#1. Count letters in a word
#👉 Input: "banana"
# 👉 Output: {'b':1, 'a':3, 'n':2}
#🎯 Teaches:
#building a hash map
#updating counts

def letter_counter():
    char_list = input("Insert your word: ")

    count = {}

    for char in char_list:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(letter_counter())    