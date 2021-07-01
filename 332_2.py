# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 10:29
# @Author  : zxl
# @FileName: 332_2.py


class Solution:

    def dfs(self,dic,n,lst ):
        if len(lst) == n:
            return True

        if lst[-1] not in dic:
            return False
        cur_pos = lst[-1]
        for i in range(len(dic[cur_pos])):
            if dic[cur_pos][i][1] == 0:
                continue

            lst.append(dic[cur_pos][i][0])
            dic[cur_pos][i][1]-=1
            f = self.dfs(dic,n,lst)
            if f :
                return f
            dic[cur_pos][i][1]+=1
            lst.pop()


        return False

    def findItinerary(self, tickets )  :

        dic = {}
        for x,y in tickets:
            if x not in dic:
                dic[x] = []
            dic[x].append([y,1])

        for x in dic:
            dic[x].sort()
        lst = ['JFK']
        n = len(tickets)+1
        self.dfs(dic,n,lst )
        return lst

obj = Solution()
tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

ans = obj.findItinerary(tickets)
print(ans)





