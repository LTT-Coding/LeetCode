#LeetCode: https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not str(x)[0].isnumeric():
            return False

        if not ("".join(reversed(str(x)))) == str(x):
            return False

        return True
