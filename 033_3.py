# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 14:59
# @Author  : zxl
# @FileName: 033_3.py


class Solution:

    def search(self, nums, target):


        lo = 0
        hi = len(nums)-1

        while lo<=hi:

            mid = (lo+hi)//2

            if nums[mid] == target:
                return mid
            if nums[mid]<=nums[hi]:
                if target>nums[mid] and target<=nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if target>=nums[lo] and target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1

        return -1


obj = Solution()
nums = [3,5,-1]
target = 3
ans = obj.search(nums,target)
print(ans)