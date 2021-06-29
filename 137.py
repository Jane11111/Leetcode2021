# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 11:09
# @Author  : zxl
# @FileName: 137.py



class Solution:
    def singleNumber(self, nums ) :

        arr = [0 for i in range(32)]

        for num in nums:

            for i in range(32):
                n = num%2
                num>>=1
                arr[i]+=n
        ans = 0
        for i in range(32):
            if arr[i]%3 :
                if i == 31:
                    ans -= 2**i
                else:
                    ans+= 2**i
        return ans

obj = Solution()
nums = [-2,-2,1,1,4,1,4,4,-4,-2]
ans = obj.singleNumber(nums)
print(ans)