# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 10:11
# @Author  : zxl
# @FileName: 682.py


class Solution:
    def calPoints(self, ops) -> int:

        self.st = []
        for c in ops:
            if c == '+':
                self.st.append(self.st[-1]+self.st[-2])
            elif c=='D':
                self.st.append(2*self.st[-1])
            elif c=='C':
                self.st.pop()
            else:
                self.st.append(int(c))
        return sum(self.st)


obj = Solution()
ops = ["1"]
ans = obj.calPoints(ops)
print(ans)
