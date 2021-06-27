# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 16:03
# @Author  : zxl
# @FileName: 433.py


# DFS

class Solution:


    def dfs(self,start, end,valided_dic,visited_dic, num):
        if start == end:
            return num

        if start in visited_dic:
            return visited_dic[start]
        visited_dic[start] = -1
        ans = float('inf')
        for i in range(len(start)):
            for c in ['A','T','C','G']:
                if start[i] == c:
                    continue
                new_s = start[:i]+c+start[i+1:]
                if new_s in valided_dic:
                    cur_num =  self.dfs(new_s,end,valided_dic,visited_dic,num+1)
                    if cur_num!=-1:
                        ans = min(ans,cur_num)
        if ans == float('inf'):
            ans = -1
        visited_dic[start] = ans
        return ans




    def minMutation(self, start: str, end: str, bank ) -> int:

        # bank.append(end)

        valided_dic = {item:True for item in bank}

        ans = self.dfs(start,end,valided_dic,{},0)
        return ans




obj = Solution()
start = "AACCGGTT"
end = "AACCGGTA"
bank = []

ans = obj.minMutation(start,end,bank)
print(ans)