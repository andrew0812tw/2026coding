# week12-3.py 學習計畫 Graph - DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected) # 先知道有幾個 Nodes
        visited = set()

        def helper(now):
            visited.add(now)
            for k in range(N):
                # 如果 k 還沒去過，且 now 與 k 是連接的 (isConnected[now][k] == 1)
                if k not in visited and isConnected[now][k]:
                    helper(k)

        ans = 0
        for i in range(N):
            if i not in visited:
                ans += 1 # 發現一個新的朋友圈（連通分量）
                helper(i) # 使用 DFS 把這個朋友圈裡的所有人都標記為 visited

        return ans
