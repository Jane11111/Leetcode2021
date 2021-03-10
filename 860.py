# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 15:51
# @Author  : zxl
# @FileName: 860.py


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        wallets=[0,0,0]

        for bill in bills:

            if bill == 5:
                wallets[0]+=1
            elif bill == 10:
                wallets[1]+=1
            else:
                wallets[2]+=1

            payback = bill-5
            if payback == 0:
                continue
            # if sum(wallets)<payback:
            #     return False
            m1 = payback//20
            m2 = (payback- m1*20)//10
            m3 = (payback-m1*20-m2*10)//5

            left = 0
            if m1 >0:
                if wallets[2]>=m1:
                    wallets[2]-=m1
                else:
                    left = m1-wallets[2]
                    wallets[2] = 0

            m2+= left*2
            left = 0
            if m2 >0:
                if wallets[1]>=m2:
                    wallets[1]-=m2
                else:
                    left = m2-wallets[1]
                    wallets[1] = 0

            m3 += left*2
            # if m1 >0:
            #     if bills[0] >= m3:
            wallets[0]-=m3
                # else:
                #     bills[0] =0
            if wallets[0] < 0:
                return False
        return True

obj = Solution()
bills = [5,5,5,10,5,5,10,20,20,20]
res = obj.lemonadeChange(bills)
print(res)