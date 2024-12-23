

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minoperation(arr):
            n = len(arr)
            if n <= 1:
                return 0
            sorted_arr = sorted(arr)
            index_map = {val: idx for idx, val in enumerate(sorted_arr)}  
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or arr[i] == sorted_arr[i]:
                    continue
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = index_map[arr[j]]  
                    cycle_size += 1
                swaps += cycle_size - 1
            return swaps

        q = deque([root])
        result = 0
        while q:
            level = [] 
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result += minoperation(level)
        return result
