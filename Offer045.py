# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 11:57
# @Author  : zxl
# @FileName: Offer045.py


class Solution:

    def quick_sort(self,nums,s,e):
        if s>=e:
            return
        x = self.partition(nums,s,e)
        self.quick_sort(nums,s,x-1)
        self.quick_sort(nums,x+1,e)


    def partition(self,nums,s,e):

        num = nums[e]
        p = s-1
        for i in range(s,e):
            if nums[i]+num<num+nums[i]:
                nums[p+1],nums[i] = nums[i],nums[p+1]
                p+=1
        nums[p+1],nums[e] = nums[e],nums[p+1]
        return p+1


    def minNumber(self, nums ) -> str:

        lst = [str(n) for n in nums]

        self.quick_sort(lst,0,len(lst)-1)
        s = ''
        for num in lst:
            s+=num
        return s

obj = Solution()
nums = [10,2]
ans = obj.minNumber(nums)
print(ans)

