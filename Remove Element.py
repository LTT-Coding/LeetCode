#LeetCode: https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if not nums[j] == val:
                nums[i] = nums[j]
                i = i + 1

        return i

