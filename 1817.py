# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 10:26
# @Author  : zxl
# @FileName: 1817.py


class Solution:
    def findingUsersActiveMinutes(self, logs , k: int) :

        dic = {}

        for uid,time in logs:

            if uid not in dic:
                dic[uid] = set([])
            dic[uid].add(time)
        arr = [0 for i in range(k)]

        for uid in dic:

            l = len(dic[uid])
            arr[l-1]+=1
        return arr