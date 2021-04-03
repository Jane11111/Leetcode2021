# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 09:37
# @Author  : zxl
# @FileName: 376.py


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lst = [nums[0]]
        i = 1
        while i<len(nums):

            if nums[i]>lst[-1]:
                while i+1<len(nums) and nums[i]<=nums[i+1]:
                    i+=1

            elif nums[i]<lst[-1]:
                while i+1<len(nums) and nums[i]>=nums[i+1]:
                    i+=1
            else:
                i+=1
                continue

            lst.append(nums[i])
            i+=1
        return len(lst)

obj = Solution()
nums = [1,2,3,4,5,6,7,8,9]
ans = obj.wiggleMaxLength(nums)
print(ans)