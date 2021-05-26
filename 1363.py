# -*- coding: utf-8 -*-
# @Time    : 2021-05-20 15:17
# @Author  : zxl
# @FileName: 1363.py




class Solution:
    def largestMultipleOfThree(self, digits ) -> str:

        digits.sort()

        sum_val = 0
        for num in digits:
            sum_val+=num

        pop_lst = []
        if sum_val%3 == 1:
            lst1 = []
            lst2 = []
            for i in range(len(digits)):
                num = digits[i]
                if num%3 ==1:
                    lst1.append(i)
                    break
                elif num%3 == 2 and len(lst2)<2:
                    lst2.append(i)
            if len(lst1) >0:
                pop_lst = lst1
            else:
                pop_lst = lst2
        elif sum_val%3 == 2:

            lst1 = []
            lst2 = []
            for i in range(len(digits)):
                num = digits[i]
                if num%3 == 1 and len(lst1)<2:
                    lst1.append(i)
                elif num%3 == 2 and len(lst2)<1:
                    lst2.append(i)
                if len(lst1)==2 and len(lst2) == 1:
                    break
            if len(lst2)==1:
                pop_lst = lst2
            else:
                pop_lst = lst1

        if (sum_val%3 != 0 and len(pop_lst) == 0) or len(pop_lst)==len(digits):
            return ''

        s = ''
        for i in range(len(digits)-1,-1,-1):
            if i not in pop_lst:
                s+=str(digits[i])
        i = 0
        while i<len(s) and s[i] == '0':
            i+=1
        s = s[i:]
        if len(s) == 0:
            s = '0'
        return s



obj = Solution()
digits = [9,8,6,8,6]
ans = obj.largestMultipleOfThree(digits)
print(ans)


