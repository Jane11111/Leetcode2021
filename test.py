# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 14:44
# @Author  : zxl
# @FileName: test.py


def deleteItem(lst):
    lst.pop(0)


l = [1,2,3,4]
l.pop(0)
deleteItem(l)
print(l)