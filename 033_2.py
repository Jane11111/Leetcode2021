# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 14:31
# @Author  : zxl
# @FileName: 033_2.py



class Solution:


    def bi_search(self,nums,i,j,target):

        if i>j:
            return -1

        if i==j :
            if nums[i] == target:
                return i
            else:
                return -1

        mid = (i+j)//2

        if nums[mid] == target:
            return mid
        lo = i
        hi = j
        if nums[mid]<=nums[j]:

            if nums[j] == target:
                return j
            if nums[j]>target:
                if nums[mid]>target:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                lo = i
                hi = mid-1
        else:

            if nums[i]== target:
                return i
            if nums[i]>target:
                lo = mid+1
            else:
                if nums[mid]>target:
                    hi = mid-1
                else:
                    lo = mid+1
        return self.bi_search(nums,lo,hi,target)






    def search(self, nums , target ) :


        return self.bi_search(nums,0,len(nums)-1,target)

obj = Solution()
nums = [3,1]
target = 4
ans = obj.search(nums,target)
print(ans)





