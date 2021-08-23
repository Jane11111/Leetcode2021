# -*- coding: utf-8 -*-
# @Time    : 2021-08-18 20:09
# @Author  : zxl
# @FileName: Huawei04.py






import sys


def solve(M,N,mat,x1,y1,x2,y2):

    dis = []

    for i in range(M):
        dis.append([[float('inf')-1000, float('inf')-1000,float('inf')-1000,float('inf')-1000 ]for j in range(N)])

    for idx in range(4):
        newx,newy =[[x1+1,y1],[x1,y1-1],[x1-1,y1],[x1,y1+1]][idx]

        if newx<0 or newy<0 or newx>=M or newy>=N or mat[newx][newy]!=0:
            continue
        dis[newx][newy][idx] = 1

    for k in range(M*N*M*N):
        for i in range(M):
            for j in range(N):
                # if i == 2 and j == 1 and dis[2][0][0] == 1:
                #     print('i am here ')
                if mat[i][j]!=0:
                    continue
                for idx in range(4): # 当前点往4个方向走
                    newx, newy = [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]][idx]
                    if newx < 0 or newy < 0 or newx >= M or newy >= N or mat[newx][newy]!=0:
                        continue

                    if idx == 0 :
                        dis[i][j][0] = min(dis[i][j][0],min(dis[newx][newy][0],1+dis[newx][newy][1],
                                                             1 + dis[newx][newy][2] ,
                                                             1 + dis[newx][newy][3] ))
                        # dis[i][j][1] = min(dis[i][j][1], dis[newx][newy][1]+1)
                        # dis[i][j][2] = min(dis[i][j][2], dis[newx][newy][2]+1)
                        # dis[i][j][3] = min(dis[i][j][3], dis[newx][newy][3]+1)
                    if idx == 1 :
                        # dis[i][j][0] = min(dis[i][j][0],dis[newx][newy][0]+1)
                        dis[i][j][1] = min(dis[i][j][1], min(dis[newx][newy][1],1+dis[newx][newy][0],
                                                             1 + dis[newx][newy][2] ,
                                                             1 + dis[newx][newy][2] ))
                        # dis[i][j][2] = min(dis[i][j][2], dis[newx][newy][2]+1)
                        # dis[i][j][3] = min(dis[i][j][3], dis[newx][newy][3]+1)
                    if idx == 2  :
                        # dis[i][j][0] = min(dis[i][j][0],dis[newx][newy][0]+1)
                        # dis[i][j][1] = min(dis[i][j][1], dis[newx][newy][1]+1)
                        dis[i][j][2] = min(dis[i][j][2], min(dis[newx][newy][2],1+dis[newx][newy][0],
                                                             1 + dis[newx][newy][1] ,
                                                             1 + dis[newx][newy][3] ))
                        # dis[i][j][3] = min(dis[i][j][3], dis[newx][newy][3]+1)
                    if idx == 3  :
                        # dis[i][j][0] = min(dis[i][j][0],dis[newx][newy][0]+1)
                        # dis[i][j][1] = min(dis[i][j][1], dis[newx][newy][1]+1)
                        # dis[i][j][2] = min(dis[i][j][2], dis[newx][newy][2]+1)
                        dis[i][j][3] = min(dis[i][j][3], min(dis[newx][newy][3],1+dis[newx][newy][0],
                                                             1 + dis[newx][newy][1] ,
                                                             1 + dis[newx][newy][2] ))
    ans = [float('inf')-1000,float('inf')-1000,float('inf')-1000,float('inf')-1000]
    for idx in range(4):
        newx, newy = [[x2 - 1, y2], [x2, y2 + 1], [x2 + 1, y2], [x2, y2 - 1]][idx]
        if newx < 0 or newy < 0 or newx >= M or newy >= N or mat[newx][newy] != 0:
            continue
        if idx == 0:
            ans[0] = min(ans[0], min(dis[newx][newy][0],1+dis[newx][newy][1] ,
                                                             1 + dis[newx][newy][2]  ,
                                                             1 + dis[newx][newy][3]  ))
            # ans[1] = min(ans[1], dis[newx][newy][1] + 1)
            # ans[2] = min(ans[2], dis[newx][newy][2] + 1)
            # ans[3] = min(ans[3], dis[newx][newy][3] + 1)
        if idx == 1:
            # ans[0] = min(ans[0], dis[newx][newy][0]+1)
            ans[1] = min(ans[1], min(dis[newx][newy][1],1+dis[newx][newy][0] ,
                                                             1 + dis[newx][newy][2] ,
                                                             1 + dis[newx][newy][2]  ))
            # ans[2] = min(ans[2], dis[newx][newy][2] + 1)
            # ans[3] = min(ans[3], dis[newx][newy][3] + 1)
        if idx == 2:
            # ans[0] = min(ans[0], dis[newx][newy][0]+1)
            # ans[1] = min(ans[1], dis[newx][newy][1] + 1)
            ans[2] = min(ans[2], min(dis[newx][newy][2],1+dis[newx][newy][0],
                                                             1 + dis[newx][newy][1] ,
                                                             1 + dis[newx][newy][3] ))
            # ans[3] = min(ans[3], dis[newx][newy][3] + 1)
        if idx == 3:
            # ans[0] = min(ans[0], dis[newx][newy][0]+1)
            # ans[1] = min(ans[1], dis[newx][newy][1] + 1)
            # ans[2] = min(ans[2], dis[newx][newy][2] + 1)
            ans[3] = min(ans[3], min(dis[newx][newy][3],1+dis[newx][newy][0],
                                                             1 + dis[newx][newy][1] ,
                                                             1 + dis[newx][newy][2] ) )
    return min(ans)


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    M,N = list(map(int, line.split()))

    mat = []

    for i in range(M):
        line = sys.stdin.readline().strip()

        arr = list(map(int, line.split()))
        mat.append(arr)

    line = sys.stdin.readline().strip()

    x1,y1,x2,y2 = list(map(int, line.split()))
    ans = solve(M,N,mat,x1,y1,x2,y2)
    print(ans)

