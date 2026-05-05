
#3. Find repeated characters
#👉 Input: "abcab"
# 👉 Output: "a" , "b"
#🎯 Teaches:
#detecting duplicates early

word = input("Enter your word: ").lower()

def char_counter():
    count = {}
    duplicates = []
    
    for char in word:
        if char in count:
            count[char] += 1
            
            if count[char] == 2:
                duplicates.append(char)
        else:
            count[char] = 1
            
    return duplicates


print(char_counter())
