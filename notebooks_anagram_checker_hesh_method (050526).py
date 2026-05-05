def anagram_checker():
    first_word = list(input("What is your first word: "))
    second_word = list(input("What is your second word: "))

    if len(first_word) !=  len(second_word):
        return False
        
    count = {} #Dictionary (Hash Map)
        
    for char in first_word:
        if char in count: #{'a': 1, 'p': 2, 'l': 1, 'e': 1}
            count[char] += 1
        else:
            count[char] = 1  #This is the first time I see this character, so its count is 1

    for char in second_word:
        if char not in count:
            return False 
        else:    
            count[char] -= 1 #{'l':0, 'i':0, 's':0, 't':0, 'e':0, 'n':0}
    
    for value in count.values():
        if value != 0:
            return False
        else:
            return True

print(anagram_checker())

        
