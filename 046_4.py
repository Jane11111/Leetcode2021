# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 11:29
# @Author  : zxl
# @FileName: 046_4.py


class Solution:


    def recPremute(self,nums,visited,lst,ans):
        if len(lst) == len(nums):
            ans.append(lst.copy())
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                lst.append(nums[i])
                self.recPremute(nums,visited,lst,ans)
                lst.pop()
                visited[i] = False


    def permute(self, nums ) :

        visited = [False for i in range(len(nums))]
        lst = []
        ans = []
        self.recPremute(nums,visited,lst,ans)
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.permute(nums)
print(ans)