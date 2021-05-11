# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 22:24
# @Author  : zxl
# @FileName: 090_3.py



class Solution:

    def subsetsWithDup(self, nums ) :

        nums.sort()

        ans = [[]]
        i = 0
        while i<len(nums):
            j = i+1
            while j<len(nums) and nums[j] == nums[j-1]:
                j+=1

            cur_lst = []
            for k in range(1,j-i+1):
                cur_lst.append([nums[i] for m in range(k)])

            l = len(ans)
            for k in range(l):
                for sub_lst in cur_lst:
                    tmp = ans[k][:]
                    tmp.extend(sub_lst)
                    ans.append(tmp)

            i = j
        return ans
obj = Solution()
nums = [1,2,2]
ans = obj.subsetsWithDup(nums)
print(ans)
