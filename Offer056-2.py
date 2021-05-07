# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 13:20
# @Author  : zxl
# @FileName: Offer056-2.py


class Solution:
    def singleNumber(self, nums ) :

        arr = [0 for i in range(32)]

        for num in nums:
            for i in range(32):
                arr[i]+=(num>>i)%2

        ans = 0
        for i in range(32):
            ans += (arr[i]%3)<<i
        return ans

obj = Solution()
nums = [9,1,7,9,7,9,7]
ans = obj.singleNumber(nums)
print(ans)


