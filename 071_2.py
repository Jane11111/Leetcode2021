# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 16:18
# @Author  : zxl
# @FileName: 071_2.py

class Solution:
    def simplifyPath(self, path: str) -> str:

        lst = []

        i = 0
        while i<len(path):

            while i<len(path) and path[i] == '/':
                i+=1
            if i>=len(path):
                break

            j = i
            while j<len(path) and path[j]!='/':
                j+=1

            p = path[i:j]
            if p == '..':
                if len(lst):
                    lst.pop()
            elif p == '.':
                pass
            else:
                lst.append(p)


            i = j
        s = '/'.join(lst)
        s = '/'+s
        return s


obj = Solution()
path = '/home//foo/'
ans = obj.simplifyPath(path)
print(ans)
