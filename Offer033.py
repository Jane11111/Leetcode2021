# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 13:45
# @Author  : zxl
# @FileName: Offer033.py

class Solution:


    def solve(self,nums,i,j,min_val,max_val):
        if i>j:
            return True

        if i==j:
            return nums[i]>=min_val and nums[i]<=max_val

        cur = nums[j]
        if cur<min_val or cur>max_val:
            return False

        k = j-1
        while k>=i and nums[k]>=cur:
            k-=1


        f1 = self.solve(nums,i,k,min_val,cur)
        f2 = self.solve(nums,k+1,j-1,cur,max_val)
        return f1 and f2




    def verifyPostorder(self, postorder ):


        min_val = float('-inf')
        max_val = float('inf')
        return self.solve(postorder,0,len(postorder)-1,min_val,max_val)


obj = Solution()
posterior = [1,6,3,2,5]
ans = obj.verifyPostorder(posterior)
print(ans)











