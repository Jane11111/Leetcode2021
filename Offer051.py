# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 10:21
# @Author  : zxl
# @FileName: Offer051.py


class Solution:

    def merge_sort(self,nums,l,r):
        if l>=r:
            return 0
        m = (l+r)//2
        count = 0
        count += self.merge_sort(nums,l,m)+self.merge_sort(nums,m+1,r)
        count+=self.merge(nums,l,m,r)
        return count

    def merge(self,nums,l,m,r):
        lst1 = nums[l:m+1]
        lst2 = nums[m+1:r+1]

        lst1.append(float('inf'))
        lst2.append(float('inf'))
        p = l
        i = 0
        j = 0
        count = 0
        while p<=r:

            n1 = lst1[i]
            n2 = lst2[j]
            if n2<n1:
                nums[p] = n2
                j+=1
                count+=(m-l+1-i)
            else:
                nums[p] = n1
                i+=1
            p+=1
        return count



    def reversePairs(self, nums) -> int:

        ans = self.merge_sort(nums,0,len(nums)-1)
        return ans




obj = Solution()
nums = [7,5,6,4]
ans = obj.reversePairs(nums)
print(ans)