# -*- coding: utf-8 -*-
# @Time    : 2021-04-03 10:39
# @Author  : zxl
# @FileName: 503.py

class Solution:
    def nextGreaterElements(self, nums):

        n = len(nums)

        r_lst = []
        r_arr = [-1 for i in range(2*n)]

        for i in range(2*n):
            if len(r_lst) == 0 or nums[i]<=nums[r_lst[-1]]:
                r_lst.append(i)
            else:
                while len(r_lst) > 0 and nums[i]>nums[r_lst[-1]]:
                    r_arr[r_lst[-1]] = nums[i]
                    r_lst.pop()
                r_lst.append(i)
            nums.append(nums[i])

        return r_arr[:n]

obj = Solution()
nums = [1,2,1]
ans = obj.nextGreaterElements(nums)
print(ans)


        



