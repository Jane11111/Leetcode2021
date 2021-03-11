# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 21:36
# @Author  : zxl
# @FileName: 275.py

class Solution(object):


    def bisearch(self,citations,p,q):
        if p>q:
            return 0
        if p==q:
            if citations[p]>=len(citations)-p:
                return len(citations)-p
        m = (p+q)//2

        if citations[m]>=len(citations)-m:
            h = self.bisearch(citations,p,m-1)
            h = max(len(citations)-m,h)
        else:
            h = self.bisearch(citations,m+1,q)
        return h

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        h = self.bisearch(citations,0,len(citations)-1)
        return h

obj = Solution()
citations = [0,1,3,5,6]
ans = obj.hIndex(citations)
print(ans)
