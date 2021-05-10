# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 17:46
# @Author  : zxl
# @FileName: 047_2.py


class Solution:


    def recursivePermute(self,nums,visited):

        i = 0
        ans = []
        while i<len(nums):
            if not visited[i]:
                visited[i] = True
                lst = self.recursivePermute(nums,visited)
                for sub_lst in lst:
                    sub_lst.insert(0,nums[i])
                    ans.append(sub_lst)
                visited[i] = False

                i+=1
                while i<len(nums) and nums[i] == nums[i-1]:
                    i+=1
            else:
                i+=1
        if len(ans) ==0:
            ans.append([])
        return ans



    def permuteUnique(self, nums ) :


        visited = {i:False for i in range(len(nums))}

        nums.sort()
        ans = self.recursivePermute(nums,visited)
        return ans

obj = Solution()
nums = [1,1,2,2]
ans = obj.permuteUnique(nums)
print(ans)