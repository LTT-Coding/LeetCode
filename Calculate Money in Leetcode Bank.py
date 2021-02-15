#LeetCode: https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 0
        day = 1
        endProduct = 0
        for i in range(n):
            if day == 8:
                monday += 1
                day = 1

            endProduct += monday + day
            day += 1

        return endProduct

