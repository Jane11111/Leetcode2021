# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 19:53
# @Author  : zxl
# @FileName: 735.py


class Solution:
    def asteroidCollision(self, asteroids )  :

        lst = []
        for i in range(len(asteroids)):
            if len(lst) == 0 or (lst[-1]<0 and asteroids[i]>0) or lst[-1]*asteroids[i]>0 :
                lst.append(asteroids[i])
            else:

                while len(lst) > 0 and asteroids[i]*lst[-1] < 0 and abs(asteroids[i]) > abs(lst[-1]):
                        lst.pop()
                if len(lst) > 0:
                    if asteroids[i]*lst[-1]>0:
                        lst.append(asteroids[i])
                    else:
                        if abs(asteroids[i]) == abs(lst[-1]):
                            lst.pop()
                else:
                    lst.append(asteroids[i])
        return lst

obj = Solution()
asteroids = [-2,-1,1,2]
ans = obj.asteroidCollision(asteroids)
print(ans)


