# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 22:58
# @Author  : zxl
# @FileName: 187_2.py


class Solution:

    def stoi(self,s):
        num = 0
        base = 0
        for i in range(len(s)):
            if s[i] == 'A':
                n = 0
            elif s[i] == 'T':
                n = 1
            elif s[i] == 'C':
                n = 2
            else:
                n = 3
            num+=n*(2**base)
            base+=2
        return num
    def itos(self,num):

        s = ''
        while len(s)<10:
            n = num%4
            if n == 0:
                s+='A'
            elif n==1:
                s+='T'
            elif n==2:
                s+='C'
            else:
                s+='G'
            num = num//4
        return s





    def findRepeatedDnaSequences(self, s: str) :

        dic = {}
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            n = self.stoi(tmp)
            if n not in dic:
                dic[n] = 1
            else:
                dic[n]+=1

        lst = []
        for k in dic:
            if dic[k]>1:
                tmp = self.itos(k)
                lst.append(tmp)
        return lst


