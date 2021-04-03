# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 13:58
# @Author  : zxl
# @FileName: 874.py

class Solution(object):


    def nextAfterObstacle(self,s,e,lst):

        new_e = e
        if e>s:
            # if (min(lst)>s and m) and e<=max(lst):
            for k in lst:
                if k>s and k<=e:
                    new_e = k-1
                    break
        elif e<s:
            # if s>=min(lst) and s<=max(lst):
            for j in range(len(lst)):
                k = lst[j]
                if k<s and k>=e:
                    new_e = k+1
                    break
        else:
            new_e = e
        return new_e


    def getNext(self,x,y,commands,cur_direction,x_dic,y_dic):
        new_direction = cur_direction
        if commands == -2:
            new_direction = (cur_direction+3)%4
        elif commands == -1:
            new_direction = (cur_direction+1)%4
        else:
            origin_x = x
            origin_y = y
            if cur_direction == 0:
                y+=commands
                if x in x_dic:
                    y = self.nextAfterObstacle(origin_y,y,x_dic[x])
            elif cur_direction == 1:
                x+=commands
                if y in y_dic:
                    x = self.nextAfterObstacle(origin_x,x,y_dic[y])
            elif cur_direction == 2:
                y-=commands
                if x in x_dic:
                    y = self.nextAfterObstacle(origin_y, y, x_dic[x])
            else:
                x-=commands
                if y in y_dic:
                    x = self.nextAfterObstacle(origin_x,x,y_dic[y])
        return new_direction,(x,y)


    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        ans = 0


        x_dic = {}
        y_dic = {}
        for x,y, in obstacles:
            if x not in x_dic:
                x_dic[x] = []
            if y not in y_dic:
                y_dic[y] = []
            x_dic[x].append(y)
            y_dic[y].append(x)
        for k in x_dic:
            x_dic[k].sort()
        for k in y_dic:
            y_dic[k].sort()

        cur_direction = 0
        x, y = 0, 0
        for command in commands:
            origin_x,origin_y = x,y
            cur_direction, (x,y) = self.getNext(x,y,command,cur_direction,x_dic,y_dic)
            if origin_x == x:
                ans = max(ans,x**2+max(origin_y**2,y**2))
            else:
                ans = max(ans,y**2+max(origin_x**2,x**2))
        return ans


commands = [7,-2,-2,7,5]
obstacles = [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]
obj = Solution()
ans = obj.robotSim(commands,obstacles)
print(ans)
