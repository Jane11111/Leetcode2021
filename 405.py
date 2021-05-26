# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 15:41
# @Author  : zxl
# @FileName: 405.py


class Solution:



    def arr2str(self,arr,dic):
        s = ''
        for i in range(31,0,-4):
            num = arr[i-3]*(2**3) + arr[i-2]*(2**2) + arr[i-1]*(2**1) + arr[i]
            s =dic[num]+s
        i = 0
        while i<len(s) and s[i] == '0':
            i+=1
        s = s[i:]
        if len(s) == 0:
            s = '0'
        return s


    def toHex(self, num: int) -> str:


        arr = [0 for i in range(32)]

        if num<0:
            arr[0] = 1
            num = 2**31+num
        for i in range(31,0,-1):
            arr[i] = num%2
            num //=2
        dic = {i:str(i) for i in range(10)}
        dic[10] = 'a'
        dic[11] = 'b'
        dic[12] = 'c'
        dic[13] = 'd'
        dic[14] = 'e'
        dic[15] = 'f'
        ans = self.arr2str(arr,dic)
        return ans

num = -1
obj = Solution()
ans = obj.toHex(num)
print(ans)
