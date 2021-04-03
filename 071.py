# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 20:05
# @Author  : zxl
# @FileName: 071.py


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        lst = []
        lst.append(path[0])
        i = 0
        while i<len(path):

            i += 1
            while i<len(path) and path[i] == '/':
                i+=1

            s = ''
            while i<len(path) and path[i] != '/':
                s+=path[i]
                i+=1
            if len(s) == 0:
                continue
            if s == '.':
                pass
            elif s == '..':
                if len(lst)>1:
                    lst.pop(-1)
            else:
                lst.append(s)
        ans = '/'
        for i in range(1,len(lst)):
            ans+=lst[i]+'/'
        if len(ans) > 1:
            ans= ans[:-1]
        return ans
obj = Solution()
path = "/a/./b/../../c/"
ans = obj.simplifyPath(path)
print(ans)

