# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 14:55
# @Author  : zxl
# @FileName: 075_3.py



class Solution:
    def sortColors(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr = [0,0,0]

        for num in nums:
            arr[num] += 1

        p_lst = [0,arr[0],arr[0]+arr[1]]

        i = 0

        while i<len(nums):

            num = nums[i]
            if num>=3:
                i+=1
                continue

            if p_lst[num] ==i:
                i+=1

                p_lst[num] += 1
            else:
                idx = p_lst[num]
                nums[i],nums[idx] = nums[idx],nums[i]
                nums[idx] +=3
                p_lst[num]+=1
        for i in range(len(nums)):
            nums[i] = nums[i]%3


obj = Solution()
nums = [2,0,1]
ans = obj.sortColors(nums)
print(nums)