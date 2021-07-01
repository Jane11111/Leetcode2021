# -*- coding: utf-8 -*-
# @Time    : 2021-06-30 22:12
# @Author  : zxl
# @FileName: 321_2.py


class Solution:

    def findlst(self,nums,count):

        if count == 0:
            return []
        lst = []
        n = len(nums)
        for i in range(len(nums)):

            num = nums[i]
            while len(lst)>0 and num>lst[-1] and len(lst)+n-i>count:
                lst.pop()
            lst.append(num)

        return lst[:count]
    def merge(self,lst1,lst2):
        lst = []
        i = 0
        j = 0
        while i<len(lst1) or j<len(lst2):

            if i >= len(lst1):
                while j<len(lst2):
                    lst.append(lst2[j])
                    j+=1
            elif j>=len(lst2):
                while i<len(lst1):
                    lst.append(lst1[i])
                    i+=1
            else:
                if lst1[i]>lst2[j]:
                    lst.append(lst1[i])
                    i+=1
                elif lst1[i]<lst2[j]:
                    lst.append(lst2[j])
                    j+=1
                else:
                    e1 = i
                    e2 = j
                    while e1<len(lst1) and e2<len(lst2) and lst1[e1] == lst2[e2]:
                        e1+=1
                        e2+=1

                    if e1 == len(lst1):
                        lst.append(lst2[j])
                        j+=1
                    elif e2 == len(lst2):
                        lst.append(lst1[i])
                        i+=1
                    elif lst1[e1]>lst2[e2]:
                        lst.append(lst1[i])
                        i+=1
                    elif lst2[e2]>lst1[e1]:
                        lst.append(lst2[j])
                        j+=1
        return lst

    def maxNumber(self, nums1 , nums2 , k: int) :


        ans = [-1 for i in range(k)]

        for l1 in range(k+1):
            l2 = k-l1
            if l1>len(nums1) or l2>len(nums2):
                continue

            lst1 = self.findlst(nums1,l1)
            lst2 = self.findlst(nums2,l2)

            lst = self.merge(lst1,lst2)

            for i in range(k):
                if ans[i]>lst[i]:
                    break
                if lst[i]>ans[i]:
                    ans = lst
                    break
        return ans

obj = Solution()
nums1 = [7,6,1,9,3,2,3,1,1]
nums2 = [4,0,9,9,0,5,5,4,7]
k = 9
ans = obj.maxNumber(nums1,nums2,k)
print(ans)
# lst1 = [9,3,2,3,1,1]
# lst2 = [9,9,7]
# ans = obj.merge(lst1,lst2)
# print(ans)
#
#
#
#
#
#
#
#
#
