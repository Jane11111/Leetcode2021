# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 16:09
# @Author  : zxl
# @FileName: 649.py

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        baned = [False for i in range(len(senate))]

        R_indices = []
        D_indices = []
        for i in range(len(senate)):
            if senate[i] == 'R':
                R_indices.append(i)
            else:
                D_indices.append(i)


        R_baned = 0
        D_baned = 0
        while True:

            i = 0
            j = 0

            for k in range(len(senate)):

                if baned[k]:
                    continue
                else:
                    if senate[k] == 'R':

                        while j< len(D_indices) and (D_indices[j]<k or baned[D_indices[j]] ):
                            j+=1
                        if j<len(D_indices):
                            baned[D_indices[j]] = True
                            j+=1
                            D_baned += 1
                        else:
                            j = 0
                            while j< len(D_indices) and baned[D_indices[j]]:
                                j+=1
                            if j< len(D_indices):
                                baned[D_indices[j]] = True
                                j+=1
                                D_baned += 1

                    else:

                        while i<len(R_indices) and (R_indices[i]<k or baned[R_indices[i]]):
                            i+=1
                        if i<len(R_indices):
                            baned[R_indices[i]] = True
                            i+=1
                            R_baned +=1
                        else:
                            i = 0
                            while i<len(R_indices) and baned[R_indices[i]]:
                                i+=1
                            if i < len(R_indices):
                                baned[R_indices[i]] = True
                                i+=1
                                R_baned+=1


                if D_baned == len(D_indices):
                    return "Radiant"
                if R_baned == len(R_indices):
                    return "Dire"


obj = Solution()
senate = "D"
ans = obj.predictPartyVictory(senate)
print(ans)