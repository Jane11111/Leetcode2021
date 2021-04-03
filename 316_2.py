# -*- coding: utf-8 -*-
# @Time    : 2021-04-01 21:32
# @Author  : zxl
# @FileName: 316_2.py


class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        lst = []
        dic = {}
        existed = set()
        for a in s:
            if a not in dic:
                dic[a] = 0
            dic[a] += 1
        for a in s:

            if a not in existed:
                while len(lst) > 0 and lst[-1]> a and dic[lst[-1]]>0:
                    existed.remove(lst.pop(-1))
                existed.add(a)
                lst.append(a)
            dic[a]-=1
        return ''.join(lst)

obj = Solution()
s = "bbcaac"
ans = obj.removeDuplicateLetters(s)
print(ans)




