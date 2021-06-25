# -*- coding: utf-8 -*-
# @Time    : 2021-06-24 21:52
# @Author  : zxl
# @FileName: 417.py



class Solution:


    def dfs4equal(self,i,j,m,n,heights,mat,visited,num):

        # if i == 11 and j == 2:
        #     print('i am here')
        # if mat[i][j]==num:
        #     return
        if visited[i][j]:
            return
        up = [i-1,j]
        left = [i,j-1]
        bottom = [i+1,j]
        right = [i,j+1]
        visited[i][j] = True

        mat[i][j] = num
        if up[0]>=0 and heights[up[0]][up[1]] == heights[i][j]:
            self.dfs4equal(up[0],up[1],m,n,heights,mat,visited,num)
        if left[1]>=0 and heights[left[0]][left[1]] == heights[i][j]:
            self.dfs4equal(left[0],left[1],m,n,heights,mat,visited,num)
        if right[1]<n and heights[right[0]][right[1]] == heights[i][j]:
            self.dfs4equal(right[0],right[1],m,n,heights,mat,visited,num)
        if bottom[0]<m and heights[bottom[0]][bottom[1]] == heights[i][j]:
            self.dfs4equal(bottom[0],bottom[1],m,n,heights,mat,visited,num)


    def dfs(self,i,j,m,n,heights, mat):

        # if i == 11 and j == 2:
        #     print('i am here')

        if mat[i][j]!=-1:
            return

        mat[i][j] = 3

        can_reach = set([])

        up = [i-1,j]
        left = [i,j-1]
        bottom = [i+1,j]
        right = [i,j+1]

        x,y = up
        if x<0:
            can_reach.add(0)
        else:
            if heights[x][y] < heights[i][j]:
                can_reach.add(mat[x][y])
            elif heights[x][y] == heights[i][j]:
                if mat[x][y] == -1:
                    self.dfs(x,y,m,n,heights,mat)
                can_reach.add(mat[x][y])
        x,y = left
        if y<0:
            can_reach.add(0)
        else:
            if heights[x][y] < heights[i][j]:
                can_reach.add(mat[x][y])
            elif heights[x][y] == heights[i][j]:
                if mat[x][y] == -1:
                    self.dfs(x,y,m,n,heights,mat)
                can_reach.add(mat[x][y])
        x,y = right
        if y>=n:
            can_reach.add(1)
        else:
            if heights[x][y] < heights[i][j]:
                can_reach.add(mat[x][y])
            elif heights[x][y] == heights[i][j]:
                if mat[x][y] == -1:
                    self.dfs(x,y,m,n,heights,mat)
                can_reach.add(mat[x][y])

        x, y = bottom
        if x >= m:
            can_reach.add(1)
        else:
            if heights[x][y] < heights[i][j]:
                can_reach.add(mat[x][y])
            elif heights[x][y] == heights[i][j]:
                if mat[x][y] == -1:
                    self.dfs(x, y, m, n, heights, mat)
                can_reach.add(mat[x][y])
        num = -2
        if 2 in can_reach or (1 in can_reach and 0 in can_reach):
            num = 2
        elif 1 in can_reach:
            num = 1
        elif 0 in can_reach:
            num = 0

        mat[i][j] = num

        return


    def pacificAtlantic(self, heights ) :

        lst = set([])
        dic = {} # 坐标
        mat = [] # -1 未探索过， -2 哪都不能去，0 左上，1 右下， 2 both, 3 visiting
        visited = []
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            mat.append([-1 for j in range(n)])
            visited.append([False for j in range(n)])
            for j in range(n):
                lst.add(heights[i][j])
                if heights[i][j] not in dic:
                    dic[heights[i][j]] =[]
                dic[heights[i][j]].append([i,j])

        lst = list(lst)
        lst.sort()

        for num in lst:
            for i,j in dic[num]:

                self.dfs(i,j,m,n,heights,mat)

                tmp = mat[i][j]
                # mat[i][j] = 3
                self.dfs4equal(i,j,m,n,heights,mat,visited,tmp) # TODO 要把登高线上的点都变成一样的

        ans = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 2:
                    ans.append([i,j])
        return ans


obj = Solution()
heights = [[18,16,12,13,6],[19,17,9,5,19],[16,16,0,4,2],[8,17,6,17,2],[5,2,13,9,10],[16,6,11,5,19],[8,6,3,12,8],[11,1,5,7,14],[6,4,14,17,12],[17,8,19,8,2],[8,5,12,10,6],[8,15,17,5,11],[0,17,17,3,3],[4,10,4,6,10],[9,4,7,10,2],[0,7,6,0,11],[3,6,10,10,11],[7,7,2,18,17],[16,14,8,6,9],[0,19,7,17,19],[4,4,4,11,13],[0,5,12,18,16],[9,2,12,16,15],[6,10,2,17,15],[7,10,7,16,18],[10,3,14,10,17],[14,2,1,1,3],[11,19,3,14,2],[11,7,7,3,6],[8,0,17,1,10],[5,3,7,15,12],[6,4,1,13,11],[0,18,9,5,15],[14,2,4,13,6],[6,17,15,2,18],[18,10,12,1,10],[8,1,4,18,1],[9,9,11,18,3],[7,16,2,3,1],[5,15,15,1,6],[0,17,5,5,1],[19,2,15,15,18],[14,18,7,5,0],[8,1,10,2,16],[6,11,19,6,15],[3,19,9,17,8],[0,5,11,12,18],[16,15,16,16,14],[2,17,2,4,17],[7,15,17,12,17],[4,1,19,10,2],[19,16,14,6,10],[1,8,0,1,15],[0,15,3,0,2],[2,3,10,13,6],[9,4,3,0,1],[6,18,11,17,1],[8,13,13,4,4]]
ans = obj.pacificAtlantic(heights)
print(ans)




