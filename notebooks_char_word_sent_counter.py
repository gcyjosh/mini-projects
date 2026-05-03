def counter():
    sentence = input("Give me a sentence: ")
    words = word_counter(sentence)
    characters = char_counter(sentence)
    sentences = sen_counter(sentence)
    print("Words:", words)
    print("Characters:", characters)
    print("Sentences:", sentences)

# count characters
def char_counter(sentence):
    return len(sentence)

# count words
def word_counter(sentence):
    words = sentence.split()
    return len(words)

# count sentences
def sen_counter(sentence):
    count = 0
    for char in sentence:
        if char in ['.', '!', '?']:
            count += 1
    return count

counter()