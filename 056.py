# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 09:19
# @Author  : zxl
# @FileName: 056.py


class Solution(object):


    def bubble_sort(self,intervals):

        for i in range(len(intervals)-1,0,-1):
            for j in range(0,i,1):
                if intervals[j+1]<intervals[j]:
                    tmp = intervals[j+1]
                    intervals[j+1] = intervals[j]
                    intervals[j] = tmp



    def insert_sort(self,intervals):
        for i in range(1,len(intervals)):
            for j in range(i-1,-1,-1):
                if intervals[j]>intervals[j+1]:
                    tmp = intervals[j]
                    intervals[j] = intervals[j+1]
                    intervals[j+1] = tmp

    def build_heap(self,intervals):
        for i in range(len(intervals)//2,-1,-1):
            self.max_heapify(intervals,i,len(intervals)-1)


    def max_heapify(self,intervals,i,heap_size):
        if i==heap_size:
            return

        left = (i+1)*2-1
        right = left+1

        p = i
        if left<=heap_size and intervals[left]>intervals[p]:
            p = left
        if right<=heap_size and intervals[right]>intervals[p]:
            p = right
        if p!=i:
            intervals[i],intervals[p] = intervals[p],intervals[i]
            self.max_heapify(intervals,p,heap_size)


    def heap_sort(self,intervals):
        self.build_heap(intervals)
        for i in range(len(intervals)-1,0,-1):
            tmp = intervals[i]
            intervals[i] = intervals[0]
            intervals[0] = tmp

            self.max_heapify(intervals,0,i-1)

    def partition(self,intervals,p,q):

        x = intervals[q]
        i = p-1
        for j in range(p,q):
            if intervals[j]<x:
                intervals[i+1],intervals[j] = intervals[j],intervals[i+1]
                i+=1
        intervals[i+1],intervals[q] = intervals[q],intervals[i+1]
        return i+1



    def quick_sort(self,intervals,p,q):
        if p>=q:
            return
        r = self.partition(intervals,p,q)
        self.quick_sort(intervals,p,r-1)
        self.quick_sort(intervals,r+1,q)



    def merge4sort(self,intervals,p,r,q):
        max_val = 100000
        l1 = intervals[p:r+1]
        l1.append([max_val,max_val])
        l2 = intervals[r+1:q+1]
        l2.append([max_val,max_val])

        i = 0
        j = 0
        while p<=q:
            if l1[i]<l2[j]:
                intervals[p]= l1[i]
                i+=1
            else:
                intervals[p] = l2[j]
                j+=1
            p+=1



    def merge_sort(self,intervals,i,j):
        if i>=j:
            return
        m = (i+j)//2
        self.merge_sort(intervals,i,m)
        self.merge_sort(intervals,m+1,j)
        self.merge4sort(intervals,i,m,j)



    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # intervals.sort() # 28ms
        # self.bubble_sort(intervals) # 5744ms
        # self.insert_sort(intervals) # 6976ms
        # self.merge_sort(intervals,0,len(intervals)-1) # 52ms
        # self.heap_sort(intervals) # 56ms
        self.quick_sort(intervals,0,len(intervals)-1) # 48ms

        ans = []

        i = 0
        while i<len(intervals):

            left_bound = intervals[i][0]
            right_bound = intervals[i][1]
            i+=1
            while i<len(intervals) and intervals[i][0]<=right_bound:
                right_bound = max(right_bound,intervals[i][1])
                i+=1
            ans.append([left_bound,right_bound])
        return ans

obj = Solution()
intervals = [[4,5],[1,4],[0,1]]
ans = obj.merge(intervals)
print(ans)