# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 15:02
# @Author  : zxl
# @FileName: 165_2.py



class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:

        i = 0
        j = 0

        while i<len(version1) or j <len(version2):

            if i>=len(version1):
                num1 = 0

            else:
                e1 = i
                while e1<len(version1) and version1[e1]!='.':
                    e1+=1
                num1 = int(version1[i:e1])
                i = e1+1

            if j>=len(version2):
                num2 = 0
            else:
                e2 = j
                while e2<len(version2) and version2[e2]!='.':
                    e2+=1
                num2 = int(version2[j:e2])
                j = e2+1

            if num1>num2:
                return 1
            if num1<num2:
                return -1
        return 0

obj = Solution()
version1 = "1.02"
version2 = "1.001"
ans = obj.compareVersion(version1,version2)
print(ans)


