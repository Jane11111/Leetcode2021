# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 14:02
# @Author  : zxl
# @FileName: 047_5.py

class Solution:

    def recFind(self,nums,visited,lst,ans):

        if len(lst) == len(nums):
            ans.append([item for item in lst])
            return

        i = 0
        while i<len(nums):
            if not visited[i]:
                lst.append(nums[i])
                visited[i] = True
                self.recFind(nums,visited,lst,ans)
                visited[i] = False
                lst.pop()
                i+=1
                while i<len(nums) and nums[i] == nums[i-1]:
                    i+=1
            else:
                i+=1

    def permuteUnique(self, nums )  :
        nums.sort()

        lst = []
        ans = []
        visited = {i:False for i in range(len(nums))}
        self.recFind(nums,visited,lst,ans)
        return ans





