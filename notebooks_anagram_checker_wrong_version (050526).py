#6. Anagram Checker
#Check if two strings are anagrams
#👉 "listen" vs "silent"
#💡 Try:
#sorting
#hash map (better)


#input first string as a variable, convert into list
#input second string as a variable, convert into list

#do two loops to ensure they are accurate, if else it.


anagram = False

def anagram_checker():
    first_word = list(input("What is your first word: "))
    second_word = list(input("What is your second word: "))

    for char in first_word:
        for char2 in second_word:
            if first_word[char] == second_word[char2] #Nested loop logic is incorrect, every char in word1 against every char in word2
                anagram = True
            else 
                anagram = False
    return anagram

anagram_checker()
    
