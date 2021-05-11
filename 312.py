# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 15:20
# @Author  : zxl
# @FileName: 312.py

# 超时

class Solution:


    def recursiveSolve(self,nums,i,j,left_bound,right_bound,dic):

        if i>j:
            return 0


        if i in dic and j in dic[i] and left_bound in dic[i][j] and right_bound in dic[i][j][left_bound]:
            return dic[i][j][left_bound][right_bound]
        if i==j:
            if i not in dic:
                dic[i] = {}
            if j not in dic[i]:
                dic[i][j] = {}
            if left_bound not in dic[i][j]:
                dic[i][j][left_bound] = {}
            dic[i][j][left_bound][right_bound] = nums[i]*left_bound*right_bound
            return dic[i][j][left_bound][right_bound]
        max_val = 0
        for k in range(i,j+1):
            l = self.recursiveSolve(nums,i,k-1,left_bound,nums[k],dic)
            r = self.recursiveSolve(nums,k+1,j,nums[k],right_bound,dic)
            max_val = max(max_val,l+r+nums[k]*left_bound*right_bound)
        if i not in dic:
            dic[i] = {}
        if j not in dic[i]:
            dic[i][j] = {}
        if left_bound not in dic[i][j]:
            dic[i][j][left_bound] = {}
        dic[i][j][left_bound][right_bound] = max_val
        return max_val


    def maxCoins(self, nums ) :

        ans = self.recursiveSolve(nums,0,len(nums)-1,1,1,{})
        return ans

obj = Solution()
nums = [3,1,5,8]
ans = obj.maxCoins(nums)
print(ans)






