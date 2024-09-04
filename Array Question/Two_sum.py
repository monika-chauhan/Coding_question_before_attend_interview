def Two_sum(nums,target):
    d = {}
    res = []
    for i, val in enumerate(nums):
        if target - val in d:
            res.append((d[target-val], i) )

        d[val] = i 
    return res if res else -1 

nums = [2,3,4,1,5]
print(Two_sum(nums,6))