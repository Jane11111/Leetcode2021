# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 10:52
# @Author  : zxl
# @FileName: 1817_2.py



class Solution:
    def findingUsersActiveMinutes(self, logs , k: int) :

        logs.sort()

        arr = [0 for i in range(k)]

        i = 0
        while i<len(logs):

            uid,time = logs[i]

            j = i+1
            count = 1
            while j<len(logs) and logs[j][0] == uid:
                if logs[j][1]!=logs[j-1][1]:
                    count+=1

                j+=1
            arr[count-1]+=1
            i = j
        return arr
