def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2

        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])

        i = j = k = 0 
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    
    return nums 

nums = [4,3,1,5,7,8]
print(merge_sort(nums))
    