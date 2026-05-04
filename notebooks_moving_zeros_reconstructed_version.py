#4. Move Zeros
#Move all 0s to the end
#Keep order of other elements

#👉 [0,1,0,3,12] → [1,3,12,0,0]

numberList = []


# input a number and do a list
number = int(input("What is your number? "))
while number != 999:
    numberList.append(number)
    number = int(input("What is your number? "))

nonZero = []
count = 0
for num in numberList:
    if num == 0:
        count += 1
    else:
        nonZero.append(num)
        
result = nonZero + [0] * count

print(result)