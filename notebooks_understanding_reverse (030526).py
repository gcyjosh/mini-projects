
def palindrome_word():
    word = input("What is your word: ")
    new_word = word.lower()
    return new_word == new_word[::-1]

print(palindrome_word())  

num = int(input("What is your number: "))
reversed_num = int(str(num)[::-1])
print(reversed_num)