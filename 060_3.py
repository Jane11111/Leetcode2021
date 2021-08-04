# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 13:01
# @Author  : zxl
# @FileName: 060_3.py


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        lst = [1,1]
        for i in range(2,n+1):
            lst.insert(0,lst[0]*i)
        lst.insert(0,-1)

        ans = ''
        nums = [i for i in range(1,n+1)]

        for i in range(1,n+1):



            a = k//lst[i+1]
            b = k%lst[i+1]
            k = b

            idx = a + (1 if b else 0 ) -1

            ans+= str(nums[idx])
            nums.pop(idx)
            if b == 0:
                while len(nums):
                    ans+= str(nums[-1])
                    nums.pop()
                break
        return ans



