nums = [0,5,6,7,0,5]

def count_nums(nums): 
    count = 0 #Use one pointer to place non-zero numbers
    for i in range(len(nums)):
        if nums[i] != 0: 
            nums[count] = nums[i] 
            #Overwrite the array in-place
            count += 1 
    for i in range(count,len(nums)): 
        nums[i] = 0 #Fill remaining spots with 0s
    return nums
    
print(count_nums(nums))