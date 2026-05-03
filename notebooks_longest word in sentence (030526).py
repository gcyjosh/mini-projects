#2. Longest Word in Sentence
#Input: string
#Output: longest word



# input string
sentence = list(input("Insert your sentence: ").split())


# create variable sentence as an array
def longest_word_filter(): 
# create variable longest_word 
    longest_word = sentence[0]
    for i in range(len(sentence)):
        if len(sentence[i]) > len(sentence[i-1]): #cannot put i+1 as i+1 is out of range
            longest_word = sentence[i]
    print(longest_word) #print function out of for loop

longest_word_filter()

