# -*- coding: utf-8 -*-
# @Time    : 2021-03-14 17:21
# @Author  : zxl
# @FileName: 210.py


class Solution(object):

    def dfs(self,node_num,dic,visited_lst,order_lst,cur_time):

        visited_lst[node_num] = 1
        has_loop = False



        cur_time[0] += 1

        if node_num not in dic:
            order_lst[node_num] = cur_time[0]
            visited_lst[node_num] = 2
            return has_loop



        for neighbor in dic[node_num]:
            if visited_lst[neighbor] == 1:
                has_loop = True
            elif visited_lst[neighbor] == 0:
                has_loop = self.dfs(neighbor,dic,visited_lst,order_lst,cur_time)

            if has_loop :
                return has_loop
        order_lst[node_num] = cur_time[0]+1
        cur_time[0]+=1
        visited_lst[node_num] = 2
        return has_loop

    def quick_sort(self,nums,indices,p,r):
        if p >= r:
            return
        q = self.partition(nums,indices,p,r)
        self.quick_sort(nums,indices,p,q-1)
        self.quick_sort(nums,indices,q+1,r)

    def partition(self,nums,indices,p,r):

        i = p-1
        x = nums[r]
        for j in range(p,r):
            if nums[j]<=x:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
                indices[i], indices[j] = indices[j], indices[i]
        nums[i+1],nums[r] = nums[r],nums[i+1]
        indices[i+1],indices[r] = indices[r],indices[i+1]
        return i+1


    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #
        # if len(prerequisites) <= 1:
        #     return []

        dic = {}
        for arr in prerequisites:
            c1 = arr[0]
            c2 = arr[1]
            if c1 not in dic:
                dic[c1] = []
            dic[c1].append(c2)

        order_lst = [0 for i in range(numCourses)]
        visited_lst = [0 for i in range(numCourses)]
        cur_time = [0]

        for i in range(numCourses):


            if i in dic and visited_lst[i] == 0:
                has_loop = self.dfs(i,dic,visited_lst,order_lst,cur_time)
                if has_loop:
                    return []

        indices = [i for i in range(numCourses)]

        self.quick_sort(order_lst,indices,0,numCourses-1)
        return indices

obj = Solution()
numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
ans = obj.findOrder(numCourses,prerequisites)
print(ans)









