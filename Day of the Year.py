# LeetCode: https://leetcode.com/problems/day-of-the-year/
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        end = datetime.datetime.strptime(date, '%Y-%m-%d')
        end_dt = datetime.date(end.year, end.month, end.day)
        start_dt = datetime.date(end.year, 1, 1)

        counter = 0
        for n in range(int((end_dt - start_dt).days) + 1):
            counter += 1
        return counter
