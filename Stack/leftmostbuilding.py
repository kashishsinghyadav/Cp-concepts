class Solution:
    def leftmostBuildingQueries(self, h: List[int], q: List[List[int]]) -> List[int]:
        res = [-1] * len(q)
        q_by_end = [[] for _ in range(len(h))]
        stack = []
        
        for i, (a, b) in enumerate(q):
            if a > b:
                a, b = b, a
            if h[b] > h[a] or a == b:
                res[i] = b
            else:
                q_by_end[b].append((h[a], i))
        
        for i in range(len(h) - 1, -1, -1):
            for val, idx in q_by_end[i]:
                pos = self.binary_search(val, stack)
                if pos != -1:
                    res[idx] = stack[pos][1]
            
            while stack and stack[-1][0] <= h[i]:
                stack.pop()
            stack.append((h[i], i))
        
        return res

    def binary_search(self, height: int, stack: List[tuple]) -> int:
        left, right = 0, len(stack) - 1
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if stack[mid][0] > height:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best
