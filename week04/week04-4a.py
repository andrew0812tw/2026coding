# week04-4a.py (重寫 week04-2.py)
# Leetcode 1732. Find the Highest Altitude
# 找到最高的海拔高度(一直加,就好了!!!)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 # 一開始的高度是0
        for gg in gain: # Python 進階 for 迴圈: 依序取出 gg
            H += gg #現在增減的量 gain[i] 加的 H
            ans = max(ans,H) #更新最高的高度
        return ans
