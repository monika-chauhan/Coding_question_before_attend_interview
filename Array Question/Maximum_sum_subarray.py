def maxSum_subarray(nums):
    start = 0 
    curr_sum = 0 
    max_sum = float('-inf')
    for end in range(len(nums)):
        curr_sum += nums[end] 

        max_sum = max(max_sum,curr_sum)

        if curr_sum < 0:
            curr_sum = 0 
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSum_subarray(nums))