#LeetCode: https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if not nums[j] == 0:
                nums[i] = nums[j]
                i = i + 1

        for j in range(i, len(nums)):
            nums[j] = 0

        return

