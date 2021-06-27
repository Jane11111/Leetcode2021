# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 13:30
# @Author  : zxl
# @FileName: 423.py



class Solution:

    def delNum(self,dic,s,cnt):
        for c in s:
            dic[c] -=cnt

    def originalDigits(self, s: str) -> str:

        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c]+=1

        num_dic = {}
        if 'z' in dic:
            cnt = dic['z']
            self.delNum(dic,'zero',cnt)
            num_dic[0] = cnt
        if 'x' in dic and dic['x']>0:
            cnt = dic['x']
            self.delNum(dic,'six',cnt)
            num_dic[6] = cnt
        if 's' in dic and dic['s']>0:
            cnt = dic['s']
            self.delNum(dic,'seven',cnt)
            num_dic[7] = cnt

        if 'v' in dic and dic['v']>0:
            cnt = dic['v']
            self.delNum(dic,'five',cnt)
            num_dic[5] = cnt

        if 'f' in dic and dic['f']>0:
            cnt = dic['f']
            self.delNum(dic,'four',cnt)
            num_dic[4] = cnt
        if 'r' in dic and dic['r']>0:
            cnt = dic['r']
            self.delNum(dic,'three',cnt)
            num_dic[3]=cnt
        if 'w' in dic and dic['w'] >0:
            cnt = dic['w']
            self.delNum(dic,'two',cnt)
            num_dic[2] = cnt
        if 'o' in dic and dic['o']>0:
            cnt = dic['o']
            self.delNum(dic,'one',cnt)
            num_dic[1] = cnt
        if 'h' in dic and dic['h']>0:
            cnt = dic['h']
            self.delNum(dic,'eight',cnt)
            num_dic[8] = cnt
        if 'i' in dic and dic['i'] >0:
            cnt = dic['i']
            self.delNum(dic,'nine',cnt)
            num_dic[9] = cnt
        ans = ''
        for i in range(10):
            if i in num_dic:
                ans+=str(i)*num_dic[i]
        return ans