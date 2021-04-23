# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 22:55
# @Author  : zxl
# @FileName: 229_2.py


class Solution:
    def majorityElement(self, nums )  :


        x = nums[0]
        i = 1
        while i<len(nums) and nums[i]==nums[i-1]:
            i+=1
        if i==len(nums):
            return [nums[0]]
        y = nums[i]
        cx = i
        cy = 1
        i+=1
        while i<len(nums):

            if cx == 0:
                while i<len(nums) and nums[i] == y:
                    cy+=1
                    i+=1
                if i<len(nums):
                    cx=1
                    x = nums[i]
                    i+=1
                continue
            if cy == 0:
                while i<len(nums) and nums[i]==x:
                    cx+=1
                    i+=1
                if i<len(nums):
                    cy = 1
                    y = nums[i]
                    i+=1
                continue



            if nums[i]==x:
                cx +=1
            elif nums[i] == y:
                cy+=1
            else:
                cx -=1
                cy -=1
            i+=1

        cx = 0
        cy = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == x:
                cx +=1
            if nums[i] == y:
                cy+=1
        ans= []
        if cx>int(n/3):
            ans.append(x)
        if cy>int(n/3):
            ans.append(y)
        return ans

obj = Solution()
nums = [1,1,1,3,3,2,2,2]
ans = obj.majorityElement(nums)
print(ans)

