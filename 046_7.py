# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 13:58
# @Author  : zxl
# @FileName: 046_7.py


class Solution:


    def recFind(self,nums,visited,lst,ans):

        if len(lst) == len(nums):
            ans.append([item for item in lst])
            return

        for i in range(len(nums)):
            if not visited[i]:
                lst.append(nums[i])
                visited[i] = True
                self.recFind(nums,visited,lst,ans)
                visited[i] = False
                lst.pop()

    def permute(self, nums ) :
        lst = []
        ans = []
        visited = {i:False for i in range(len(nums))}
        self.recFind(nums,visited,lst,ans)
        return ans