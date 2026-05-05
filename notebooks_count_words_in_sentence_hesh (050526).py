#2. Count words in a sentence
#👉 Input: "i love python i love coding"
# 👉 Output:
#{"i":2, "love":2, "python":1, "coding":1}
#🎯 Teaches:
#splitting strings
#word frequency maps


sentence = input("Enter your sentence here: ").lower().split()

def word_counter():
    count = {}
    for char in sentence:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(word_counter())