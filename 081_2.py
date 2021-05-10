# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 15:14
# @Author  : zxl
# @FileName: 081_2.py


class Solution:


    def bisearch(self,nums,target,i,j):
        if i>j:
            return False
        if i==j:
            if nums[i] == target:
                return True
            return False

        lo = i
        hi =j

        mid = (i+j)//2

        if nums[mid] == target:
            return True

        if nums[mid] == nums[j] and nums[mid] == nums[i]:
            r = True
            for k in range(mid,j+1):
                if nums[k] != nums[mid]:
                    r = False
                    break
            if r:
                hi = mid-1
            else:
                lo = mid+1
        elif nums[mid]<=nums[j]:
            if target>nums[mid] and target<=nums[j]:
                lo = mid+1
            else:
                hi = mid-1
        else:
            if target>=nums[i] and target<nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        return self.bisearch(nums,target,lo,hi)



    def search(self, nums , target )  :

        return self.bisearch(nums,target,0,len(nums)-1)


obj = Solution()
nums = [1,1,1,1,1,2,1]
target = 2
ans = obj.search(nums,target)
print(ans)






