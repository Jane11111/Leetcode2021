# -*- coding: utf-8 -*-
# @Time    : 2021-04-07 13:47
# @Author  : zxl
# @FileName: 946.py


class Solution:
    def validateStackSequences(self, pushed, popped) :

        i = 0
        j = 0
        lst = []
        while i<len(pushed) and j<len(popped):

            while (len(lst)==0 or lst[-1] != popped[j]) and i<len(pushed):
                lst.append(pushed[i])
                i+=1

            while len(lst) > 0 and j<len(popped) and lst[-1] == popped[j]:
                lst.pop()
                j+=1
        if i == len(pushed) and j == len(popped) and len(lst) == 0:
            return True
        return False

obj = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
ans = obj.validateStackSequences(pushed,popped)
print(ans)


