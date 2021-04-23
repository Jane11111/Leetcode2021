# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 13:36
# @Author  : zxl
# @FileName: Offer031.py



class Solution:
    def validateStackSequences(self, pushed , popped )  :


        lst = []
        i = 0
        j = 0
        while i<len(pushed) and j<len(popped):


            if len(lst) == 0:
                lst.append(pushed[i])
                i+=1


            while i<len(pushed) and lst[-1] != popped[j]:
                lst.append(pushed[i])
                i+=1
            while len(lst)>0 and j<len(popped) and lst[-1] == popped[j]:
                lst.pop()
                j+=1





        return i==len(pushed) and j==len(popped)  and len(lst) == 0