# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 17:29
# @Author  : zxl
# @FileName: Offer062_2.py




class Solution:



    def lastRemaining(self, n: int, m: int) -> int:

        ans = 0


        for i in range(2,n+1):

            ans = (ans+m)%i  #以m作为0开始，i-1个数剩下ans_old作为最后一个
        return ans



obj = Solution()
n = 5
m = 3
ans = obj.lastRemaining(n,m)
print(ans)