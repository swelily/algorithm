def twoSum(nums, target):
    dict1 = { }
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict1:
            return (i, dict1[complement])
        dict1[nums[i]] = i
