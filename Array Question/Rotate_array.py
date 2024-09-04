# Rotate array 
def Rotare_array(nums, k):
    k = k % len(nums)
    temp = nums[:k]
    for i in range(k,len(nums)):
        nums[i-k] = nums[i]
    nums[k+1:] = temp 
    return nums 
nums = [1,2,3,4,5]
print(Rotare_array(nums, 2))