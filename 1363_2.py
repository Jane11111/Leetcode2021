# -*- coding: utf-8 -*-
# @Time    : 2021-05-20 15:48
# @Author  : zxl
# @FileName: 1363_2.py



class Solution:
    def largestMultipleOfThree(self, digits ) -> str:


        sum_val = 0
        freq = {}
        for num in digits:
            sum_val += num
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        lst1 = []
        lst2 = []
        for i in range(len(digits)):
            num = digits[i]
            if num %3 == 1:
                if len(lst1)<2:
                    lst1.append(i)
                else:
                    max_idx = 0
                    if digits[lst1[0]]<digits[lst1[1]]:
                        max_idx = 1
                    if digits[lst1[max_idx]]>digits[i]:
                        lst1[max_idx] = i

            elif num %3 == 2:
                if len(lst2)<2:
                    lst2.append(i)
                else:
                    max_idx = 0
                    if digits[lst2[0]]<digits[lst2[1]]:
                        max_idx = 1
                    if digits[lst2[max_idx]]>digits[i]:
                        lst2[max_idx] = i
        pop_lst = []
        if sum_val %3 == 1:
            if len(lst1)>0:
                if len(lst1)== 1 or digits[lst1[0]]<digits[lst1[1]]:
                    pop_lst.append(lst1[0])
                else:
                    pop_lst.append(lst1[1])
            elif len(lst2)>=2:
                pop_lst.extend(lst2[:2])

        elif sum_val %3 == 2:
            if len(lst2)>0:
                if len(lst2)== 1 or digits[lst2[0]]<digits[lst2[1]]:
                    pop_lst.append(lst2[0])
                else:
                    pop_lst.append(lst2[1])
            elif len(lst1)>=2:
                pop_lst.extend(lst1[:2])
        if (sum_val%3>0 and len(pop_lst) == 0) or len(pop_lst) == len(digits):
            return ''


        for idx in pop_lst:
            freq[digits[idx]] -=1

        s = ''
        for i in range(9,-1,-1):

            if i in freq:


                s+=str(i)*freq[i]




        i = 0
        while i<len(s) and s[i] == '0':
            i+=1
        if i == len(s):
            s = '0'
        else:
            s = s[i:]
        return s


obj = Solution()
digits = [8,1,9]
ans = obj.largestMultipleOfThree(digits)
print(ans)
