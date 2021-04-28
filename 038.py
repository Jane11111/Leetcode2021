# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 13:51
# @Author  : zxl
# @FileName: 038.py

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        count = 1
        s = '1'
        while count<n:


            new_s = ''
            i = 0
            while i<len(s):
                j = i+1
                while j<len(s) and s[j] == s[i]:
                    j+=1
                # num = str(s[i])
                new_s += (str(j-i)+s[i])
                i = j
            s = new_s




            count+=1
        return s

obj = Solution()
n = 5
ans = obj.countAndSay(n)
print(ans)



