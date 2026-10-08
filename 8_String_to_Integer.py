class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        sign = 1
        i = 0

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        if num < -2147483648:
            num = -2147483648
        if num > 2147483647:
            num = 2147483647

        return num
