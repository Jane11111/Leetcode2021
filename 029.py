# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 13:51
# @Author  : zxl
# @FileName: 029.py


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == 0:
            return 0

        ans = 0
        ops = 1
        if dividend<0:
            ops*=-1
            dividend = -dividend
        if divisor < 0 :
            ops*=-1
            divisor = -divisor

        sum_val = divisor
        sum_count = 1

        while dividend>=divisor:

            if dividend<sum_val:
                sum_val = divisor
                sum_count = 1
            dividend -= sum_val
            ans+=sum_count

            sum_val+=sum_val
            sum_count+=sum_count

            if (ops == 1 and ans> 2**31-1) or (ops==-1 and ans>2**31) :
                return 2**31-1
        return ans*ops

obj = Solution()
dividend = 1
divisor = 1
ans = obj.divide(dividend,divisor)
print(ans)
