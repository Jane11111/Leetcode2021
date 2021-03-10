# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 16:51
# @Author  : zxl
# @FileName: 016.py


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = 3000
        ans = 3000

        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]:
                continue

            m = i+1
            n = len(nums)-1
            while m<n:

                if nums[i]+nums[m]+nums[n]>target:
                    if abs(target-nums[i]-nums[m]-nums[n])<diff:
                        diff = abs(target-nums[i]-nums[m]-nums[n])
                        ans = nums[i]+nums[m]+nums[n]
                    n-=1
                elif nums[i]+nums[m]+nums[n]<target:
                    if abs(target-nums[i]-nums[m]-nums[n])<diff:
                        diff = abs(target-nums[i]-nums[m]-nums[n])
                        ans = nums[i]+nums[m]+nums[n]
                    m+=1
                else:
                    return target
        return ans


obj = Solution()
nums = [-1,2,1,-4]
target = 1
ans = obj.threeSumClosest(nums,target)
print(ans)