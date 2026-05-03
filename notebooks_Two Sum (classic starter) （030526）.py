#Two Sum (classic starter) Given an array and a target Return. indices of two numbers that add up to target


#input a list 
#list = input("Give me the list: ") returns a bunch of integers instead of list
nums = list(map(int, input("Enter numbers separated by space: ").split()))
#map(int, ...) : applies integer for every item
#split() : adds a comma for everything
#list() : Converts the result into a list

#input a key
key = int(input("Give me the key: "))

found = False

for i in range(len(nums)):
#    for j in range(len(list)):  might use the same element twice ❌
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == key:
            #print(i,j)
            found = True
            print("Found！")

if not found:
    print("Not found!")