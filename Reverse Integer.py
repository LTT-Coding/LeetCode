# LeetCode: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return int(x)

        reversedInt = "".join(reversed(str(x)))
        while reversedInt.startswith('0'):
            reversedInt = reversedInt.replace('0', '', 1)

        if not str(x)[0].isnumeric():
            firstLetter = str(x)[0]
            reversedInt = reversedInt.replace(firstLetter, "")
            reversedInt = firstLetter + reversedInt

        if int(reversedInt) > 2147483647 or int(reversedInt) < -2147483648:
            return 0

        return int(reversedInt)
