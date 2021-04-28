# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 18:41
# @Author  : zxl
# @FileName: 030.py


class Solution:
    def findSubstring(self, s: str, words )  :



        word_idx = [-1 for i in range(len(s))]
        word_len = len(words[0])
        dic = {}
        for i in range(len(words)):
            dic[words[i]] = i
        freq_dic = {}
        for word in words: #都用idx
            if dic[word] not in freq_dic:
                freq_dic[dic[word]] = 1
            else:
                freq_dic[dic[word]]+=1

        for i in range(len(s)):
            if s[i:i+word_len] in dic:
                word_idx[i] = dic[s[i:i+word_len]]
        ans = []
        for i in range(len(s)):
            new_freq_dic = {k:v for k,v in freq_dic.items()}
            f = True

            for j in range(i,min(i+len(words)*word_len,len(s)),word_len):
                if word_idx[j] == -1:
                    break
                if new_freq_dic[word_idx[j]] == 0:
                    break
                new_freq_dic[word_idx[j]]-=1

            for k in new_freq_dic:
                if new_freq_dic[k]!=0:
                    f = False
                    break
            if f:
                ans.append(i)




        return ans

obj = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
ans = obj.findSubstring(s,words)
print(ans)
