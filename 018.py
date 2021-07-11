# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 16:09
# @Author  : zxl
# @FileName: 018.py



class Solution:
    def fourSum(self, nums , target: int) :

        nums.sort()
        ans = []
        i = 0

        while i<len(nums):


            n1 = nums[i]

            j= i+1
            while j<len(nums):



                n2 = nums[j]

                l = j+1
                r = len(nums)-1

                while l<r:

                    if n1+n2+nums[l]+nums[r]== target:
                        ans.append([n1,n2,nums[l],nums[r]])
                        l+=1
                        while l<len(nums) and nums[l] == nums[l-1]:
                            l+=1
                    elif n1+n2+nums[l]+nums[r] < target:
                        l += 1
                        while l < len(nums) and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        r-=1
                        while r>=0 and nums[r] == nums[r+1]:
                            r-=1

                j+=1
                while j<len(nums) and nums[j] == nums[j-1]:
                    j+=1

            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
        return ans
