def Lonest_incresing_subsequence(nums):
    n = len(nums)
    LIS = [1] * (n +1)
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i],LIS[j]+1)
    return LIS[n-1]

nums = [10,9,2,5,3,7,101,18]
print(Lonest_incresing_subsequence(nums))
