# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 21:41
# @Author  : zxl
# @FileName: 492_2.py



class Solution:


    def recursiveFind(self,nums,idx, lst,ans):
        if idx == len(nums):
            if len(lst)>=2:
                ans.append(lst.copy())
            return

        if len(lst) == 0  or nums[idx]>=lst[-1] :
            lst.append(nums[idx])
            self.recursiveFind(nums,idx+1,lst,ans)
            lst.pop()
            if len(lst)==0  or nums[idx]!=lst[-1] :
                self.recursiveFind(nums,idx+1,lst,ans)

        else:
            self.recursiveFind(nums,idx+1,lst,ans)


    def findSubsequences(self, nums  ) :

        lst = []
        ans = []
        self.recursiveFind(nums,0,lst,ans)
        return ans



obj = Solution()
nums = [4,6,7,7]
ans = obj.findSubsequences(nums)
print(ans)



