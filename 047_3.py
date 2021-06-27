# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 17:15
# @Author  : zxl
# @FileName: 047_3.py


class Solution:


    def recPermute(self,nums,used,lst):
        if len(lst) == len(nums):
            return [[item for item in lst]]


        i = 0
        ans = []
        while i <len(nums):

            if not used[i]:
                lst.append(nums[i])
                used[i] = True
                cur_ans = self.recPermute(nums,used,lst)
                used[i] = False
                lst.pop()
                ans.extend(cur_ans)

                i+=1
                while i<len(nums) and nums[i] == nums[i-1]:
                    i+=1
            else:
                i+=1
        return ans



    def permuteUnique(self, nums ) :

        nums.sort()

        used = {i:False for i in range(len(nums))}
        ans = self.recPermute(nums,used,[])
        return ans
