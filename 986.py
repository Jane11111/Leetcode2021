# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 14:44
# @Author  : zxl
# @FileName: 986.py



class Solution:
    def intervalIntersection(self, firstList , secondList )  :

        i = 0
        j = 0
        ans = []
        while i<len(firstList) and j<len(secondList):


            if firstList[i][1]<secondList[j][0]:
                i+=1
            elif firstList[i][0]>secondList[j][1]:
                j+=1
            else :
                left_bound = max(secondList[j][0],firstList[i][0])
                right_bound = min(firstList[i][1],secondList[j][1])
                ans.append([left_bound,right_bound])
                if firstList[i][1]>=secondList[j][1]:
                    j+=1
                else:
                    i+=1


        return ans


obj = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
ans = obj.intervalIntersection(firstList,secondList)
print(ans)
