
def removeDuplicates(nums):
    length = len(nums)
    if length ==0 or length == 1:
        return length
    for i in range(len(nums) - 1):
        while nums[i] in nums[i+1:]:
            nums[i+1:].remove(nums[i])
    return len(nums)










