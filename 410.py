# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 14:41
# @Author  : zxl
# @FileName: 410.py


# 递归

class Solution:

    def recSplit(self,nums,idx,m,dic):

        if idx in dic and m in dic[idx]:
            return dic[idx][m]
        if m == 1:
            return sum(nums[idx:])

        if len(nums)-idx == m:
            return max(nums[idx:])

        if len(nums)-idx <m :
            return float('inf')

        ans = float('inf')
        sum_val = 0

        for i in range(idx,len(nums)):
            if sum_val+nums[i]>=ans:
                break
            sum_val+=nums[i]
            sub_min_max = self.recSplit(nums,i+1,m-1,dic)
            v = max(sum_val,sub_min_max)

            ans = min(ans,v)

        if idx not in dic:
            dic[idx] = {}
        dic[idx][m] = ans

        return ans




    def splitArray(self, nums , m: int) -> int:



        ans = self.recSplit(nums,0,m,{})
        return ans

obj = Solution()
nums = [7,2,5,10,8]
m = 2
ans = obj.splitArray(nums,m)
print(ans)



