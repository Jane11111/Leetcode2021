# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 22:09
# @Author  : zxl
# @FileName: I0105.py

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:

        if abs(len(first)-abs(len(second))) >=2:
            return False


        if len(first) == len(second):
            count = 0

            for i in range(len(first)):
                if first[i] != second[i]:
                    count+=1
            return count<=1
        if len(first)<len(second):
            first, second = second, first

        i = 0
        j = 0
        count = 0
        while i<len(first) and j<len(second):
            if first[i] == second[j]:
                i+=1
                j+=1
            else :
                i+=1
                count+=1


        return count<=1

obj = Solution()
first = 'mart'
second = 'karmt'
ans = obj.oneEditAway(first,second)
print(ans)


