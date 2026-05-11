#9. First non-repeating character
#👉 Input: "aabbcdde"
# 👉 Output: "c"
#🎯 Teaches:
#frequency + scanning


def non_repeating_char():
    word = input("What is your word:")
    
    count = {}
    
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1  
            
    for char in word: #2nd loop to include every character
        if count[char] == 1:
            print(char)
            return
        
    print(None)

non_repeating_char()