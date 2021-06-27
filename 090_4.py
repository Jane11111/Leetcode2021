# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 16:59
# @Author  : zxl
# @FileName: 090_4.py

class Solution:
    def subsetsWithDup(self, nums ) :

        nums.sort()

        i = 0
        ans = [[]]
        while i<len(nums):

            l = len(ans)
            for k in range(l):
                tmp = [item for item in ans[k]]
                tmp.append(nums[i])
                ans.append(tmp)
            i += 1
            count = 1
            while i<len(nums) and nums[i] == nums[i-1]:
                count+=1
                for k in range(l):
                    tmp = [item for item in ans[k]]
                    for j in range(count):
                        tmp.append(nums[i])
                    ans.append(tmp)
                i+=1
        return ans
obj = Solution()
nums = [1,2,2]
ans = obj.subsetsWithDup(nums)
print(ans)


