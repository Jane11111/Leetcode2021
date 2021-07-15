# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 09:53
# @Author  : zxl
# @FileName: 030_3.py


class Solution:


    def findSubstring(self, s: str, words):


        n = len(s)
        m = len(words[0])
        k = len(words)
        ans = []

        allwords_dic = {word: 0 for word in words}
        for word in words:
            allwords_dic[word]+=1


        for i in range(m):
            cur_dic = {}
            count = 0
            idx = i

            for j in range(i,n,m):

                if s[j:j+m] not in allwords_dic:
                    cur_dic = {}
                    count = 0
                    idx = j+m
                else:
                    if s[j:j+m] not in cur_dic:
                        cur_dic[s[j:j+m]] =0
                    while cur_dic[s[j:j+m]] == allwords_dic[s[j:j+m]]:
                        cur_dic[s[idx:idx+m]]-=1
                        idx+=m
                        count-=1
                    cur_dic[s[j:j+m]] += 1
                    count+=1
                if count == k:
                    ans.append(idx)
        return ans






