# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 15:42
# @Author  : zxl
# @FileName: 016_2.py


class Solution:
    def threeSumClosest(self, nums , target: int) -> int:

        nums.sort()

        sum_val = -1
        diff = float('inf')

        for i in range(len(nums)):
            num = nums[i]

            l = i+1
            r = len(nums)-1
            while l<r:
                if abs(target-num-nums[l]-nums[r])<diff:
                    diff = abs(target-num-nums[l]-nums[r])
                    sum_val = num+nums[l]+nums[r]

                if nums[l]+nums[r]<target-num:

                    l+=1
                else:
                    r-=1
            i+=1

        return sum_val


