# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 16:21
# @Author  : zxl
# @FileName: Shopee3.py


class Solution:
    def petalsBreak(self, petals) :

        ans = 0
        for num in petals:
            if num<=0:
                continue

            ans += (num//2)+num%2
        return ans

obj = Solution()
petals = [4,2,1]
ans = obj.petalsBreak(petals)
print(ans)
