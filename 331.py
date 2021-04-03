# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 20:26
# @Author  : zxl
# @FileName: 331.py


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')

        if len(preorder) == 1:
            if preorder[0] == '#':
                return True
            else:
                return False
        lst = [preorder[0]]

        i = 1
        while i<len(preorder) and len(lst)>0:
            s = lst.pop(0)
            if s == '#':
                continue

            lst.append(preorder[i])
            if i+1 >=len(preorder):
                return False
            lst.append(preorder[i+1])
            i+=2
        if i<len(preorder):
            return False
        return True

obj = Solution()
preorder = "1"
ans = obj.isValidSerialization(preorder)
print(ans)