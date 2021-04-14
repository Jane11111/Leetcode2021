# -*- coding: utf-8 -*-
# @Time    : 2021-04-04 16:55
# @Author  : zxl
# @FileName: 781.py


class Solution:
    def numRabbits(self, answers) :

        dic = {}
        for item in answers:
            if item not in dic:
                dic[item] = 0
            dic[item] += 1
        ans = 0
        for k in dic:
            v = dic[k]
            n1 = int(v/(k+1))
            if v%(k+1) :
                n1+=1
            ans += (n1)*(k+1)
        return ans

obj = Solution()
answers = [3,3,3,3,3]
ans = obj.numRabbits(answers)
print(ans)
