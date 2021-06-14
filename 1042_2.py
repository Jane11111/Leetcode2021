# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 14:55
# @Author  : zxl
# @FileName: 1042_2.py



class Solution:

    def recPlante(self,cur_id,dic,arr):
        used = [False for i in range(5)]

        undraw_count = 0
        for neighbors in dic[cur_id]:
            if arr[neighbors] !=-1:
                used[arr[neighbors]] = True
            else:
                undraw_count +=1

        f = False
        for color_num in range(1,5):
            if not used[color_num]:
                arr[cur_id] = color_num
                if undraw_count == 0:
                    f = True
                else:
                    for n_id in dic[cur_id]:
                        if arr[n_id]==-1:
                            f = self.recPlante(n_id,dic,arr)
                            if f:
                                break
                if f:
                    return f
                arr[cur_id] = -1

        return f

    def gardenNoAdj(self, n: int, paths ) :



        arr = [-1 for i in range(n)]

        dic = {i:[] for i in range(n)}
        for x, y in paths:
            dic[x-1].append(y-1)
            dic[y-1].append(x-1)


        for i in range(n):
            self.recPlante(i,dic,arr)
        return arr

obj = Solution()
n = 5
paths =  [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]
ans = obj.gardenNoAdj(n,paths)
print(ans)
