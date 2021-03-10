# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 20:15
# @Author  : zxl
# @FileName: 1718.py

class Solution(object):


    def recursiveConstruct(self,arr,valid_lst):
        if sum(valid_lst) == 0:
            return True

        idx = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                idx = i
                break

        for i in range(len(valid_lst)):
            val = valid_lst[i]
            if val == 0:
                continue
            if val == 1:
                arr[idx] = 1
                valid_lst[i] = 0
                f = self.recursiveConstruct(arr,valid_lst)
                if f:
                    return True
                arr[idx] = 0
                valid_lst[i] = val

            elif idx+val<len(arr) and arr[idx+val] == 0:
                arr[idx] = val
                arr[idx+val] = val
                valid_lst[i] = 0
                f = self.recursiveConstruct(arr,valid_lst)
                if f:
                    return True
                arr[idx] = 0
                arr[idx+val] = 0
                valid_lst[i] = val
        return False





    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        for i in range(n,0,-1):
            lst = [0 for i in range(2*n-1)]
            valid_lst = [i for i in range(n,0,-1)]
            if self.recursiveConstruct(lst,valid_lst ):
                return lst
obj = Solution()
n = 3
print(obj.constructDistancedSequence(n))