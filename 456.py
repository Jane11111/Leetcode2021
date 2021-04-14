# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 19:13
# @Author  : zxl
# @FileName: 456.py


class Solution:
    def find132pattern(self, nums) :

        last = float('-inf')

        lst = []

        for i in range(len(nums)-1,-1,-1):

            if nums[i]<last:
                return True

            while len(lst)>0 and nums[i]>lst[-1]:
                last = lst.pop()

            lst.append(nums[i])
        return False

obj = Solution()
nums = [1,2,3,4]
ans = obj.find132pattern(nums)
print(ans)




