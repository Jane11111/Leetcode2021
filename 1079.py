# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 13:46
# @Author  : zxl
# @FileName: 1079.py


class Solution(object):

    def recursiveSplit(self,tile_lst,p):

        if p == len(tile_lst):
            return 1
        i = p+1
        while i<len(tile_lst) and tile_lst[i] == tile_lst[i-1]:
            i+=1

        left_count = i-p+1
        right_count = self.recursiveSplit(tile_lst,i)
        return left_count*right_count

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tile_lst = []
        for i in range(len(tiles)):
            tile_lst.append(tiles[i])
        tile_lst.sort()

        count = self.recursiveSplit(tile_lst,0)
        return count-1



obj = Solution()
tiles = "AAB"
count = obj.numTilePossibilities(tiles)
print(count)