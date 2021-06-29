# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 13:40
# @Author  : zxl
# @FileName: 165.py

class Solution:

    def getVersion(self,version):

        arr = []
        i = 0
        while i<len(version):
            j = i
            while j<len(version) and version[j] != '.':
                j+=1
            while i<j and version[i] == '0':
                i+=1
            num = version[i:j]
            if len(num)>0:
                arr.append(int(num))
            else:
                arr.append(0)

            i = j+1
        return arr



    def compareVersion(self, version1: str, version2: str) -> int:

        arr1 = self.getVersion(version1)
        arr2 = self.getVersion(version2)

        while len(arr1)<len(arr2):
            arr1.append(0)
        while len(arr2)<len(arr1):
            arr2.append(0)

        for i in range(len(arr1)):
            if arr1[i]>arr2[i]:
                return 1
            if arr1[i]<arr2[i]:
                return -1

        return 0



obj = Solution()
version1 = "0.1"
version2 = "1.1"
ans = obj.compareVersion(version1,version2)
print(ans)










