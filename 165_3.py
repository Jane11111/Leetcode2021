# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 09:50
# @Author  : zxl
# @FileName: 165_3.py




class Solution:

    def cleanStr(self,s):
        i = 0
        while i<len(s) and s[i] == '0':
            i+=1
        s = s[i:]
        return s


    def compareVersion(self, version1: str, version2: str) -> int:


        i = 0
        j = 0
        while i<len(version1) or j<len(version2):


            if i == len(version1):
                s1 = '0'
            else:
                p = i
                while p<len(version1) and version1[p]!='.':
                    p+=1
                s1 = self.cleanStr(version1[i:p])
                i = p+1
            if j == len(version2):
                s2 = '0'
            else:
                q = j
                while q<len(version2) and version2[q]!='.':
                    q+=1
                s2 = self.cleanStr(version2[j:q])
                j = q+1

            if len(s1)> len(s2) or (len(s1) == len(s2) and s1>s2) :
                return 1
            elif len(s1)<len(s2) or (len(s1) == len(s2) and s1<s2):
                return -1
        return 0

