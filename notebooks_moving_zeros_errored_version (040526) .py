#4. Move Zeros
#Move all 0s to the end
#Keep order of other elements

#👉 [0,1,0,3,12] → [1,3,12,0,0]

numberList =[]
# input string and convert them into a list
numberList = list(input("Insert numbers: ").split()) 


for i in range(len(numberList)):#rearranging elements, breaks order
    numberList.remove("0") #len(numberList) is 3, but is inaccesible since it is removed


print(numberList)

# select 0, and rearrange indexes to be at the back

