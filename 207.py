# -*- coding: utf-8 -*-
# @Time    : 2021-03-13 22:37
# @Author  : zxl
# @FileName: 207.py


class Node():
    def __init__(self,val=0,color=0,neighbors = []):
        self.val = val
        self.color = color
        self.neighbors = neighbors



class Solution(object):

    def dfs(self,node):
        ans = False

        node.color = 1

        for neighbor in node.neighbors:
            if neighbor.color == 1:
                ans = True
            elif neighbor.color == 0:
                ans = self.dfs(neighbor)
            if ans :
                return ans

        node.color = 2
        return ans

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        node_lst = [None for i in range(numCourses)]
        for arr in prerequisites:
            c1 = arr[0]
            c2 = arr[1]
            if node_lst[c1 ] is None:
                node_lst[c1 ] = Node(c1 ,0,[])
            if node_lst[c2 ] is None:
                node_lst[c2 ] = Node(c2 ,0,[])
            node_lst[c1].neighbors.append(node_lst[c2])

        for node in node_lst:
            if node is None:
                continue
            ans = self.dfs(node)
            if ans :
                return False
        return True


numCourses = 3
prerequisites = [[0,1],[0,2],[1,0]]
obj = Solution()
ans = obj.canFinish(numCourses,prerequisites)
print(ans)

