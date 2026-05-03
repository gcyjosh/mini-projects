def palindrome_checker():
    sentence = input("Enter your sentence: ")
    
    clean_sentence = sentence.lower()
    for ch in ",.+!?:; ": #“Go through each character inside this string one by one.”, ",.+!?:; "represents the string
                            #So the loop runs like this:
                            #First loop → ch = ','
                            #Second loop → ch = '.'
        clean_sentence = clean_sentence.replace(ch, "") #“Remove that character (ch) from the sentence.”
    
    return clean_sentence == clean_sentence[::-1]

print(palindrome_checker())