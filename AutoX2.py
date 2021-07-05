# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 19:30
# @Author  : zxl
# @FileName: AutoX2.py



import sys


def solveArea(rectangles, nums,K):
    ans = 0

    for i in range(len(rectangles)):

        x1,y1,x2,y2 = rectangles[i]
        m = nums[i]
        if m<K:
            continue

        ans += abs((x2-x1)*(y2-y1))
    return ans

def pos2str(x1,y1,x2,y2):
    s = str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2)
    return s

def find(s,dic):
    # s = pos2str(x1,y1,x2,y2)
    if dic[s] == s:
        return s
    dic[s] = find(dic[s],dic)
    return dic[s]

def isConnected(y1,y2,y3,y4):
    return not (y3>=y2 or y4<=y1)

def merge(s1,s2,dic):

    dic[find(s1,dic)] = find(s2,dic)


def solveConnected(rectangles):

    rectangles.sort()

    fa = {}
    xdic = {}
    ydic= {}

    for line in rectangles:
        x1,y1,x2,y2 = line[:4]
        if x1>x2:
            x1,y1,x2,y2 = x2,y2,x1,y1

        s = pos2str(x1,y1,x2,y2)
        fa[s] = s
        if x1 not in xdic:
            xdic[x1] = []
        xdic[x1].append([s,y1,x2,y2])

        if y1<y2:
            if y1 not in ydic:
                ydic[y1] = []
            ydic[y1].append([s,x1,y2,x2])
        else:
            if y2 not in ydic:
                ydic[y2] = []
            ydic[y2].append([s,x2,y1,x1])

    for x1 in xdic:
        for line in xdic[x1]:
            s,y1,x2,y2 = line
            min_y1 = min(y1,y2)
            max_y1 = max(y1,y2)

            if x2 not in xdic:
                continue
            for line2 in xdic[x2]:
                s2,y3,x4,y4 = line2

                min_y3,max_y3 = min(y3,y4),max(y3,y4)

                if isConnected(min_y1,max_y1,min_y3,max_y3):
                    merge(s,s2,fa)
    for y1 in ydic:
        for line in ydic[y1]:
            s,x1,y2,x2 = line
            min_x1 = min(x1,x2)
            max_x1 = max(x1,x2)

            if y2 not in ydic:
                continue
            for line2 in ydic[y2]:
                s2,x3,y4,x4 = line2

                min_x3 = min(x3,x4)
                max_x3 = max(x3,x4)

                if isConnected(min_x1,max_x1,min_x3,max_x3):
                    merge(s,s2,fa)

    sets = set([])
    for k in fa:
        sets.add(find(k,fa))
    return len(sets)








if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    N , K = values
    rectangles = []
    nums = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))

        rectangles.append(values[:4])
        nums.append(values[-1])

    area = solveArea(rectangles,nums,K)
    cc = solveConnected(rectangles)
    print(area,cc)
