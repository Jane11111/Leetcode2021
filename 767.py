# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 20:57
# @Author  : zxl
# @FileName: 767.py


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) <= 1:
            return S

        dic = {}
        l = len(S)
        max_freq = l//2+l%2
        for c in S:
            if c not in dic:
                dic[c] = 0
            dic[c]+=1
            if dic[c]>max_freq :
                return ''
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        lst = [sorted_dic[0][0] for i in range(sorted_dic[0][1])]

        i = 1
        for k in range(1,len(sorted_dic)):
            c = sorted_dic[k][0]
            freq = sorted_dic[k][1]

            for m in range(freq):
                lst.insert(i,c)
                i+=2
                if i>len(lst):
                    i=0

        return ''.join(lst)

obj = Solution()
S = "aabbabcc"
ans = obj.reorganizeString(S)
print(ans)