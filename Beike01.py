# -*- coding: utf-8 -*-
# @Time    : 2021-08-13 20:55
# @Author  : zxl
# @FileName: Beike01.py



class Solution:
    def section(self , a , t ):
        # write code here
        n = len(a)
        interval_count = 0
        tmp = 0
        for i in range(len(a)):
            f = False
            for j in range(i+1,len(a)):
                if a[i]^a[j] == t:
                    f = True
                    interval_count += ((n-j)+(j)-1-tmp)
            if f:
                tmp+=1
        ans = n*(n-1)/2 - interval_count
        return ans

obj = Solution()
a = [2,3,4]
t = 6
ans = obj.section(a,t)
print(ans)