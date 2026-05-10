#8. Group anagrams (VERY IMPORTANT)
#👉 Input: ["eat","tea","tan","ate","nat","bat"]
#👉 Output:
#[["eat","tea","ate"], ["tan","nat"], ["bat"]]
# Teaches:
#hash map of lists
#grouping by computed key


def group_anagram():
    word = input("Enter a word: ")
    anagramList = []
    while word != "999":
        anagramList.append(word)
        word = input("Enter a word: ")
    print(anagramList)
    
    groups = {} #dictionary
    
    for i in anagramList:
        key = "".join(sorted(anagramList[i])) #create key
        
        if key not in groups:
            groups[key] = [] #create new list and store it in the dictionary under this ey
        groups[key].append(i)
        
    print(list(groups.values()))
    
    
group_anagram()