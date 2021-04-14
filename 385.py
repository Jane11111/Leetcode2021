# -*- coding: utf-8 -*-
# @Time    : 2021-04-04 17:28
# @Author  : zxl
# @FileName: 385.py


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:


        if len(s) == 0 or s[0] != '[':
            arr = s.split(',')
            ans = NestedInteger()
            for item in arr:
                ans.setInteger(int(item))
            return ans


        lst = []
        i = 0
        while i<len(s):
            if s[i] == '[':
                nested_lst = NestedInteger()
                if len(lst) > 0:
                    lst[-1].add(nested_lst)
                lst.append(nested_lst)
                i+=1
            elif s[i] == ']':
                    if len(lst)>1:
                        lst.pop()
                    i+=1
            elif s[i] == ',':
                i+=1
            else:
                cur_s = s[i]
                i+=1
                while i<len(s) and s[i]>='0' and s[i]<='9':
                    cur_s+=s[i]
                    i+=1
                lst[-1].setInteger(int(cur_s))

        return lst[-1]
obj = Solution()
s = "324"
ans = obj.deserialize(s)
print(ans)
