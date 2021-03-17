# -*- coding: utf-8 -*-
# @Time    : 2021-03-14 21:21
# @Author  : zxl
# @FileName: 332.py

class Solution(object):

    def dfs(self,dic,edges, s,num):

        path = [s]
        if s not in dic:
            return path


        neighbors = dic[s]
        neighbors.sort()
        for neighbor in neighbors:
            if  edges[s+neighbor] > 0:
                edges[s + neighbor] -= 1
                sub_path = self.dfs(dic,edges, neighbor,num -1)
                if num == 11:
                    print('i am here')
                if len(sub_path) != num-1 :
                    edges[s+neighbor] += 1
                else:
                    path.extend(sub_path)
                    break


        return path






    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        dic = {}
        edges = {}
        for ticket in tickets:
            s = ticket[0]
            e = ticket[1]
            if s+e not in edges:
                edges[s+e] = 0
            edges[s+e] += 1
            if s not in dic:
                dic[s] = []
            dic[s].append(e)
        ans = self.dfs(dic,edges, 'JFK',len(tickets)+1)
        return ans

obj = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
ans = obj.findItinerary(tickets)
print(ans)
