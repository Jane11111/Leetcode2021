# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 22:13
# @Author  : zxl
# @FileName: 442.py



class Solution:
    def findDuplicates(self, nums ) :

        i = 1
        ans = []
        nums.insert(0,0)

        while i<len(nums):
            num = nums[i]

            if num == i:
                i+=1
                continue

            if nums[num] == num:
                # ans.append(num)
                i+=1
            else:
                nums[i],nums[num] = nums[num],nums[i]
        for i in range(1,len(nums)):
            num = nums[i]
            if num!=i and nums[num] == num:
                ans.append(num)

        return ans

obj = Solution()
nums = [4,3,2,7,8,2,3,1]
ans = obj.findDuplicates(nums)
print(ans)
