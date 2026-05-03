#3. Valid Palindrome (harder version)
#Ignore:
#spaces
#punctuation
#case

# "A man, a plan, a canal: Panama" → True

found = False

def palindrome_checker():
    #input variable for the sentence
    sentence = input("Enter your sentence: ")

    #remove the ',' + '.' + ':'
    clean_sentence = sentence.replace(",","")
    clean_sentence = clean_sentence.replace(".","")
    clean_sentence = clean_sentence.replace(":","")
    if clean_sentence == clean_sentence[::-1]:
        found = True
        print(found)

palindrome_checker()


