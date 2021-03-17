# -*- coding: utf-8 -*-
# @Time    : 2021-03-14 17:08
# @Author  : zxl
# @FileName: 207_2.py


class Solution(object):

    def dfs(self,node_num,dic,visited_lst):

        has_loop = False

        visited_lst[node_num] = 1

        if node_num  in dic:
            for neighbor in dic[node_num]:
                if visited_lst[neighbor] == 1:
                    has_loop =True
                elif visited_lst[neighbor] == 0:
                    has_loop = self.dfs(neighbor,dic,visited_lst)
                if has_loop:
                    return has_loop
        visited_lst[node_num] = 2

        return has_loop


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        if len(prerequisites) <= 1:
            return True

        dic = {}
        for arr in prerequisites:
            c1 = arr[0]
            c2 = arr[1]
            if c1 not in dic:
                dic[c1] = []
            dic[c1].append(c2)
        visted_lst = [0 for i in range(numCourses)]
        for node_num in dic.keys():
            has_loop = self.dfs(node_num,dic,visted_lst)
            if has_loop:
                return False
        return True

numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
obj = Solution()
ans = obj.canFinish(numCourses,prerequisites)
print(ans)


