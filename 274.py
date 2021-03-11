# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 17:13
# @Author  : zxl
# @FileName: 274.py

class Solution(object):

    def quick_sort(self,nums,p,r):
        if p>=r:
            return
        q = self.partition(nums,p,r)
        self.quick_sort(nums,p,q-1)
        self.quick_sort(nums,q+1,r)

    def partition(self,nums,p,r):

        x = nums[r]
        i = p-1
        for j in range(p,r):
            if nums[j]<=x:
                nums[i+1],nums[j] = nums[j],nums[i+1]
                i+=1
        nums[i+1],nums[r] = nums[r], nums[i+1]
        return i+1


    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        self.quick_sort(citations,0,len(citations)-1)

        n = len(citations)
        for i in range(0,len(citations)):
            if citations[i]>=n:
                return n
            n-=1
        return 0

obj = Solution()
citations = [3,0,6,1,5]
ans = obj.hIndex(citations)
print(ans)
