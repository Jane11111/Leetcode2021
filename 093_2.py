# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 15:38
# @Author  : zxl
# @FileName: 093_2.py

class Solution:

    def recFind(self,s,idx,seg_count,addr,ans):
        if idx == len(s) and seg_count == 0:
            ans.append(addr[:-1])

        if seg_count == 0 or idx == len(s):
            return

        if s[idx] == '0':
            self.recFind(s,idx+1,seg_count-1,addr+s[idx]+'.',ans)
        else:
            for i in range(idx,len(s)):
                subs = s[idx:i+1]
                if len(subs)>3 or int(subs)>255:
                    break
                self.recFind(s,i+1,seg_count-1,addr+subs+'.',ans)

    def restoreIpAddresses(self, s: str) :

        ans = []
        self.recFind(s,0,4,'',ans)
        return ans



