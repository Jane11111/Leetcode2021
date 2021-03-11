# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 20:46
# @Author  : zxl
# @FileName: 042.py


class Solution(object):




    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=2:
            return 0

        arr1 = [-1 for x in height]
        lst =[]
        i = 0
        while i<len(height):
            if len(lst) == 0:
                lst.insert(0,i)
            else:
                if height[i]<height[lst[0]]:
                    lst.insert(0,i)
                else:
                    while len(lst)>0 and height[i]>=height[lst[0]]:
                        arr1[lst[0]] = i
                        lst.pop(0)
                    lst.insert(0,i)
            i+=1

        lst = []
        arr2 = [-1 for x in height]
        i = len(height)-1
        while i>= 0:
            if len(lst) == 0:
                lst.insert(0,i)
            else:
                if height[i]<height[lst[0]]:
                    lst.insert(0,i)
                else:
                    while len(lst) > 0 and height[i]>=height[lst[0]]:
                        arr2[lst[0]] =i
                        lst.pop(0)
                    lst.insert(0,i)
            i-=1

        arr = [0 for x in height]
        i = 0
        while i< len(height):
            h = height[i]
            if arr1[i] <0 or arr1[i] == i+1:
                i+=1
            else:
                idx = arr1[i]
                while i< idx:
                    arr[i]=h
                    i+=1
        i = len(height) -1
        while i>= 0:
            h = height[i]
            if arr2[i]<0 or arr2[i] == i-1:
                i-=1
            else:
                idx = arr2[i]
                while i>idx:
                    arr[i] = max(h,arr[i])
                    i-=1

        ans  = 0
        for i in range(len(height)):
            if arr[i] > 0:
                ans += (arr[i]-height[i])
        return ans

obj = Solution()
height = [4,2,0,3,2,5]
ans = obj.trap(height)
print(ans)



