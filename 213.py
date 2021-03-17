# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 11:12
# @Author  : zxl
# @FileName: 213.py


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n == 0:
            return 0
        elif n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])


        arr1 = [0 for i in range(n)] # not rob
        arr2 = [0 for i in range(n)] # rob

        # rob 0
        arr1[0] = nums[0]
        arr1[1] = nums[0]
        arr2[0] = nums[0]
        arr2[1] = nums[0]
        for i in range(2,n-1):
            arr1[i] = max(arr1[i-1],arr2[i-1])
            arr2[i] = arr1[i-1] + nums[i]
        ans = max(arr1[n-2],arr2[n-2])

        # not rob 0
        arr1[0] = 0
        arr2[0] = 0
        for i in range(1,n):
            arr1[i] = max(arr1[i-1],arr2[i-1])
            arr2[i] = arr1[i-1] + nums[i]

        ans = max([ans,arr1[n-1],arr2[n-1]])
        return ans

obj = Solution()
nums = [2,3,2]
ans = obj.rob(nums)
print(ans)





