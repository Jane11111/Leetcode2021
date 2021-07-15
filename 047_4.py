# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 13:47
# @Author  : zxl
# @FileName: 047_4.py


class Solution:


    def recurFind(self,nums,used,lst,ans):

        if len(lst) == len(nums):
            ans.append([item for item in lst])


        i = 0

        while i<len(nums):

            if not used[i]:

                lst.append(nums[i])
                used[i] = True

                self.recurFind(nums,used,lst,ans)

                lst.pop()
                used[i] = False

                i+=1
                while i<len(nums) and nums[i] == nums[i-1]:
                    i+=1


            else:
                i+=1


    def permuteUnique(self, nums ):
        nums.sort()

        used = {i:False for i in range(len(nums))}
        lst = []
        ans = []
        self.recurFind(nums,used,lst,ans)
        return ans