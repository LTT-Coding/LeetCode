#LeetCode: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in chars:
                if stack:
                    topElement = stack.pop()
                else:
                    topElement = '#'
                if chars[char] != topElement:
                    return False
            else:
                stack.append(char)

        return not stack