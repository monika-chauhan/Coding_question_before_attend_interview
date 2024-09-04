def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        left = [x for x in nums[1:] if x < pivot]
        right = [x for x in nums[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
nums = [4,3,5,7,8,3,2]
print(quick_sort(nums))