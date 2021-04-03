# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 21:21
# @Author  : zxl
# @FileName: 224.py


class Solution:

    def str2int(self,s):
        if s[0] == '+':
            return int(s[1:])
        elif s[0] == '-':
            return - int(s[1:])
        else:
            return int(s)

    def basic_calculate(self,arr):
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]

        if arr[0] == '+':
            arr.pop(0)
        elif arr[0] == '-':
            arr.pop(0)
            arr[0] = -arr[0]

        ans = int(arr[0])
        i = 1
        while i<len(arr):
            op = arr[i]
            n2 = int(arr[i+1])

            if op == '+':
                ans += n2
            else:
                ans -= n2
            i+=2
        return ans

    def calculate(self, s: str) -> int:

        s = s.replace(' ','')
        lst = []
        i = 0
        while i<len(s):
            if s[i] == '(' or s[i] == '+' or s[i] == '-':
                lst.append(s[i])
                i+=1
            elif s[i] == ')':
                new_arr = []
                while lst[-1] != '(':
                    new_arr.insert(0,lst[-1])
                    lst.pop(-1)
                lst.pop(-1)
                num = self.basic_calculate(new_arr)
                lst.append(num)
                i+=1

            else:
                cur_s = s[i]
                i+=1
                while i<len(s) and s[i]!='-' and s[i] != '+'and s[i] !='(' and s[i] != ')':
                    cur_s += s[i]
                    i+=1
                lst.append(self.str2int(cur_s))
        ans = self.basic_calculate(lst)
        return ans

obj = Solution()
s = "1 + 1"
ans = obj.calculate(s)
print(ans)



