# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 21:09
# @Author  : zxl
# @FileName: 784.py


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return ['']

        ans = []
        changed = False
        for i in range(len(S)):
            s = S[i]
            if s >='0' and s<='9':
                continue
            changed = True

            left_lst = [S[:i+1]]
            if str.isupper(s):
                left_lst.append(S[:i]+str.lower(s))
            else:
                left_lst.append(S[:i]+str.upper(s))

            right_lst = self.letterCasePermutation(S[i+1:])
            for right_str in right_lst:
                for left_str in left_lst:
                    ans.append(left_str+right_str)
            break

        if not changed:
            ans.append(S)
        return ans

obj =Solution()
S = "a1b1c"
ans = obj.letterCasePermutation(S)
print(ans)