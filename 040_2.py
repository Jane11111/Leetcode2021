# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 21:23
# @Author  : zxl
# @FileName: 040_2.py


class Solution:


    def recursiveFind(self,nums,idx,target):
        if target == 0:
            return [[]]
        if idx == len(nums) or target<0:
            return []
        ans = []
        i = idx
        while i<len(nums):
            lst = self.recursiveFind(nums,i+1,target-nums[i])
            for sub_lst in lst:
                sub_lst.insert(0,nums[i])
                ans.append(sub_lst)
            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
        return ans

    def combinationSum2(self, candidates , target: int)  :
        candidates.sort()

        ans = self.recursiveFind(candidates,0,target)
        return ans

obj = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
ans = obj.combinationSum2(candidates,target)
print(ans)






