# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 22:08
# @Author  : zxl
# @FileName: 090_2.py


class Solution:

    def recursiveFind(self,nums,idx):
        if idx == len(nums):
            return [[]]

        j = idx+1
        while j<len(nums) and nums[j] == nums[j-1]:
            j+=1

        left_lst = [[]]
        for i in range(1,j-idx+1):
            left_lst.append([nums[idx] for k in range(i)])
        right_lst = self.recursiveFind(nums,j)
        ans = []
        for lst1 in left_lst:

            for lst2 in right_lst:
                tmp = lst1[:]
                tmp.extend(lst2)
                ans.append(tmp)
        return ans


    def subsetsWithDup(self, nums ) :

        nums.sort()
        ans = self.recursiveFind(nums,0)
        return ans

obj = Solution()
nums = [1,2,2]
ans = obj.subsetsWithDup(nums)
print(ans)


