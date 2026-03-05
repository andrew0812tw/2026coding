# week02-3.py 學習計畫
# Leetcode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s),len(t) #字串的長度
        if N1==0: return True #有陷阱

        i = 0 #要記得i從0開始
        for k in range(N2):
            if s[i] == t[k]:
                i += 1
            if i==N1:
                return True
        return False
