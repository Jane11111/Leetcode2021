# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 16:07
# @Author  : zxl
# @FileName: 1042_3.py



class Solution:
    def gardenNoAdj(self, n: int, paths):


        arr = [-1 for i in range(n)]

        dic = {i:[] for i in range(n)}
        for x,y in paths:
            dic[x-1].append(y-1)
            dic[y-1].append(x-1)

        for i in range(n):

            used = {i:False for i in range(1,5)}

            for n_id in dic[i]:
                if arr[n_id]!=-1:
                    used[arr[n_id]] = True
            for c_num in used:
                if not used[c_num]:
                    arr[i] = c_num
                    break
        return arr



obj = Solution()
n = 5
paths =  [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]
ans = obj.gardenNoAdj(n,paths)
print(ans)
