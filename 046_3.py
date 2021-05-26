# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 21:54
# @Author  : zxl
# @FileName: 046_3.py
class Solution:

    def recPermute(self,nums,dic,lst,ans):

        if len(lst) == len(nums):
            ans.append(lst.copy())
            return

        for i in range(len(nums)):
            if not dic[i]:

                dic[i] = True
                lst.append(nums[i])
                self.recPermute(nums,dic,lst,ans)
                lst.pop()
                dic[i] = False

        return






    def permute(self, nums ) :

        lst = []
        ans = []
        dic = {i:False for i in range(len(nums))}
        self.recPermute(nums,dic,lst,ans)
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.permute(nums)
print(ans)