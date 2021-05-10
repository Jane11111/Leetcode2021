# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 17:34
# @Author  : zxl
# @FileName: 046_2.py


class Solution:

    def recPermute(self,nums,dic):

        ans = []
        for k in dic:
            if not dic[k]:
                num = nums[k]
                dic[k] = True
                lst = self.recPermute(nums,dic)
                dic[k] = False
                for new_lst in lst:
                    new_lst.insert(0,num)
                    ans.append(new_lst)
        if len(ans) == 0:
            ans.append([])
        return ans



    def permute(self, nums ) :


        dic = {i:False for i in range(len(nums))}

        ans = self.recPermute(nums,dic)
        return ans

obj = Solution()
nums = [1,2,3]
ans = obj.permute(nums)
print(ans)
