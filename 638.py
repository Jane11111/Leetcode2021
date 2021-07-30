# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 20:28
# @Author  : zxl
# @FileName: 638.py

class Solution:


    def recCombine(self,price,special,needs,val,idx):

        n = len(price)

        if idx == len(special):

            for i in range(len(needs)):
                val+= needs[i]*price[i]
            return val

        ans = self.recCombine(price,special,needs,val,idx+1) # 不购买当前的礼包

        stop = False
        i = 1
        while not stop: # 购买几份当前礼包
            tmp = [item for item in needs]

            money = special[idx][-1]*i

            for j in range(n):
                tmp[j]-=(i*special[idx][j])
                if tmp[j]<0:
                    stop = True
                    break
            if stop :
                break
            newans = self.recCombine(price,special,tmp,val+money,idx+1)
            ans = min(ans,newans)
            i+=1
        return ans


    def shoppingOffers(self, price , special , needs ) -> int:


        ans = self.recCombine(price,special,needs,0,0)
        return ans

obj = Solution()


price = [1,1,1]
special = [[1,1,0,0],[2,2,1,9]]
needs = [1,1,0]
ans = obj.shoppingOffers(price,special,needs)
print(ans)