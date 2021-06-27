# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 17:20
# @Author  : zxl
# @FileName: 076.py



class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq_dic = {}
        for c in t:
            if c not in freq_dic:
                freq_dic[c] = 0
            freq_dic[c]+=1
        not_cover = len(freq_dic)

        l = 0
        min_len = float('inf')
        sub_s = ''
        for r in range(len(s)):
            c = s[r]
            if c in freq_dic:
                freq_dic[c]-=1
                if freq_dic[c] == 0:
                    not_cover -=1

            while not_cover == 0: # 直到把这个窗口收缩到最小
                if r-l+1<min_len: # 找到一个更小的字串
                    min_len = r-l+1
                    sub_s = s[l:r+1]

                if s[l] in freq_dic: # 左边删除是否对当前窗口有影响
                    freq_dic[s[l]]+=1
                    if freq_dic[s[l]] == 1:
                        not_cover+=1

                l+=1
        return sub_s
