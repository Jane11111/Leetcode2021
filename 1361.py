# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 20:56
# @Author  : zxl
# @FileName: 1361.py




class Solution:

    def dfs(self,rid,leftChild,rightChild,visited):

        visited[rid] = True

        lc = leftChild[rid]
        rc = rightChild[rid]
        f1 = True
        f2 = True
        if lc!= -1:
            if visited[lc]:
                return False
            f1 = self.dfs(lc,leftChild,rightChild,visited)
        if rc!=-1:
            if visited[rc]:
                return False
            f2 = self.dfs(rc,leftChild,rightChild,visited)
        if not f1 or not f2:
            return False
        return True

    def validateBinaryTreeNodes(self, n: int, leftChild , rightChild ) -> bool:

        indegree = {i:0 for i in range(n)}
        for c in leftChild:
            if c!=-1:
                indegree[c]+=1
        for c in rightChild:
            if c!=-1:
                indegree[c]+=1

        rid = -1
        for idx in indegree:
            if indegree[idx] == 0:
                rid = idx
                break
        if rid == -1:
            return False

        visited = [False for i in range(n)]

        f = self.dfs(rid,leftChild,rightChild,visited)
        if not f:
            return f
        for idx in range(n):
            if not visited[idx]:
                return False
        return True

obj = Solution()
n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]
ans = obj.validateBinaryTreeNodes(n,leftChild,rightChild)
print(ans)
