# -*- coding: utf-8 -*-
# @Time    : 2021-07-18 17:29
# @Author  : zxl
# @FileName: Byte02.py




def solve(records):

    ans = 0
    count = 0


    for rec in records:
        uid = rec[0]
        tag = rec[1][0]
        time = rec[1][1]

        if tag == 0:
            count += 1
            ans = max(count,ans)
        else:
            count -=1
    return ans







if __name__ == '__main__':

    # lst = [['A', [0,1]],['B',[0,2]],['A',[1,3]],['B',[1,4]]]

    # lst = [['A',[0,0]],['B',[0,1]],['C',[0,2]],['A',[1,3]]]

    lst = [['A',[0,0]],['B',[0,1]],['C',[0,2]],['D',[0,3]]]

    # lst = [1,2,3]
    ans = solve(lst)
    print(ans)