class Solution:
    def rotate(self, nums, k) -> None:
        k = k%len(nums)
        nums = nums[-k:] + nums[:-k-1]