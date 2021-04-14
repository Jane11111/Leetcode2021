# -*- coding: utf-8 -*-
# @Time    : 2021-04-08 09:24
# @Author  : zxl
# @FileName: 347.py


class Solution:

    def minHeapify(self,arr,i):

        smallest = i
        if 2*i+1<len(arr) and arr[2*i+1][1]<arr[i][1]:
            smallest = 2*i+1
        if 2*i+2<len(arr) and arr[2*i+2][1]<arr[smallest][1]:
            smallest = 2*i+2
        if smallest != i:
            arr[i],arr[smallest] = arr[smallest],arr[i]
            self.minHeapify(arr,smallest)

    def buildHead(self,arr):
        n= len(arr)
        for i in range(int(n/2)-1,-1,-1):
            self.minHeapify(arr,i)
    def insertHeap(self,arr,tup):

        arr[0] = tup
        self.minHeapify(arr,0)





    def topKFrequent(self, nums, k) :

        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        ans = []
        count = 0
        for i in dic:
            count += 1
            if count == k:
                ans.append([i,dic[i]])
                self.buildHead(ans)
            elif count < k:
                ans.append([i,dic[i]])
            else:
                if dic[i]<=ans[0][1]:
                    continue
                else:
                    self.insertHeap(ans,[i,dic[i]])

        res = [item[0] for item in ans]
        return res

obj = Solution()
nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
k = 7
ans = obj.topKFrequent(nums,k)
print(ans)



