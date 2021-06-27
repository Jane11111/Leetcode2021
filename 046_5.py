# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 17:10
# @Author  : zxl
# @FileName: 046_5.py


class Solution:


    def recPermute(self,nums,used,lst):
        if len(lst) == len(nums):
            return [[item for item in lst]]
        ans = []

        for i in range(len(nums)):
            num = nums[i]
            if not used[i]:
                lst.append(num)
                used[i] = True
                cur_ans = self.recPermute(nums,used,lst)
                ans.extend(cur_ans)
                used[i] = False
                lst.pop()
        return ans



    def permute(self, nums )  :
        used = {i:False for i in range(len(nums))}


        ans = self.recPermute(nums,used,[])
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.permute(nums)
print(ans)