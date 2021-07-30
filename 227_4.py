# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 19:30
# @Author  : zxl
# @FileName: 227_4.py



class Solution:

    def recCal(self,s,idx,val,last_op,last_val):
        if idx == len(s):
            return val

        op = s[idx]

        i = idx+1
        while i<len(s) and s[i].isdigit():
            i+=1

        num = int(s[idx+1:i])

        if op == '+':
            return self.recCal(s,i,val+num,'+',num)
        elif op == '-':
            return self.recCal(s,i,val-num, '-',num)
        else:
            if op == '*':
                cur_val = last_val*num
            else:
                cur_val = last_val//num

            if last_op == '-':
                new_val = val+last_val-cur_val
            else:
                new_val = val-last_val+cur_val

            return self.recCal(s,i,new_val,last_op,cur_val)


    def calculate(self, s: str) -> int:

        i = 0
        s = s.replace(' ','')
        while i<len(s) and s[i].isdigit():
            i+=1

        val = int(s[:i])
        ans = self.recCal(s,i,val,'+',val)
        return ans

obj = Solution()
s = " 3+5 / 2 "
ans = obj.calculate(s)
print(ans)





