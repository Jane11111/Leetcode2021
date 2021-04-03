# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 20:17
# @Author  : zxl
# @FileName: 216.py

class Solution(object):

    def recursiveFind(self,nums,k,n):
        ans = []
        if k==0 and n== 0:
            ans.append([])
            return ans
        elif n!=0 and (k==0 or len(nums) == 0):
            return ans

        for i in range(len(nums)):
            num = nums[i]
            sub_ans_lst = self.recursiveFind(nums[i+1:],k-1,n-num)
            for sub_ans in sub_ans_lst:
                sub_ans.insert(0,num)
                ans.append(sub_ans)
        return ans

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        lst = [i for i in range(1,10)]
        ans = self.recursiveFind(lst,k,n)
        return ans

obj = Solution()
k = 3
n = 9
ans = obj.combinationSum3(k,n)
print(ans)