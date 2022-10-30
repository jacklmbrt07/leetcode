class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            res[i] = left
            left = left * nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]

        return res
