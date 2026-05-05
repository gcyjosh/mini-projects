
#🧠 What the problem is asking

#You are given:

#An array of numbers
#A number k (window size)

#👉 You must find:

#the maximum sum of any consecutive k elements


nums = []
number = int(input("Insert your number: "))

while number != 999:
    nums.append(number)
    number = int(input("Insert your number: "))

key = int(input("Insert your key: "))

# Step 1: first window
maxSum = sum(nums[0:key])
new_maxSum = maxSum

# Step 2: slide window
for i in range(key,len(nums)):
    maxSum = maxSum - nums[i - key] + nums[i]
    if maxSum > new_maxSum:
        new_maxSum = maxSum
        
        
print(new_maxSum)


