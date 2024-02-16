
nums = [1,2,3,4,5]

def sum_list(nums):
    if len(nums) ==1:
        return nums[0]
    
    return nums[0] + sum_list(nums[1:])

print(sum_list(nums))