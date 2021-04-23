# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 23:01
# @Author  : zxl
# @FileName: Offer011.py


class Solution:


    def biSearch(self,numbers,l,h):
        if l == h:
            return numbers[l]
        m = int((l+h)/2)

        if numbers[m+1] <numbers[h] and numbers[l]<numbers[m]:
            return min(numbers[l],numbers[m+1])

        if numbers[l]>numbers[m]:
            return self.biSearch(numbers,l,m)
        if numbers[m+1]>numbers[h]:
            return self.biSearch(numbers,m+1,h)
        return min(self.biSearch(numbers,l,m),self.biSearch(numbers,m+1,h))



    def minArray(self, numbers ) :
        n = len(numbers)
        l = 0
        h = n-1

        num = self.biSearch(numbers,l,h)
        return num

obj = Solution()
numbers = [2,2,2,0,1]
ans = obj.minArray(numbers)
print(ans)