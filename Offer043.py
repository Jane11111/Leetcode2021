# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 16:08
# @Author  : zxl
# @FileName: Offer043.py


class Solution:
    def countDigitOne(self, n: int) -> int:

        if n==0:
            return 0

        if n<10:
            return 1

        count = 0
        num = n
        lst = []
        last_val_lst = [0] # 例12345,sum_val_lst = [12345,2345,345,45,5,0], lst=[1,2,3,4,5]
        while num:
            lst.insert(0,num%10)
            last_val_lst.insert(0,num%10*(10**(len(last_val_lst)-1))+last_val_lst[0])
            count+=1
            num//=10
        # sum_val_lst.pop()
        first_val_lst = [0]
        base_lst = [1]
        for num in lst:
            first_val_lst.append(first_val_lst[-1]*10+num)
            base_lst.append(base_lst[-1]*10)
        first_val_lst[0] = 1
        # first_val_lst.pop(1)
        # last_val_lst.pop()


        base_lst[0] = 0
        base_lst.insert(0,0)

        dp = [0 for i in range(count+1)] # 位数与对应1个数
        dp[1] = 1
        for i in range(2,count+1):
            dp[i] = dp[i-1]*9+10**(i-1)+dp[i-1]

        ans = dp[count-1]

        for i in range(count):

            if i!=count-1:
                n1 = 10**(count-i-1)
            else:
                n1 = 1

            m1 = first_val_lst[i]-base_lst[i]
            if base_lst[i]>=10:
                m1+=1
            if lst[i] >1:
                ans+=n1*m1
            else:
                ans+=n1*(m1-1)



            if lst[i] == 1:
                n2 = last_val_lst[i+1 ] +1
            else:
                n2 = 0


            ans+=n2



        return ans

obj = Solution()
n = 103
ans = obj.countDigitOne(n)
print(ans)


