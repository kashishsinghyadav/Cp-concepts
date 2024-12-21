class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            nonlocal max_components
            subtree_sum = values[node]

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                subtree_sum += dfs(neighbor, node)

            if subtree_sum % k == 0:
                max_components += 1
                return 0 
            return subtree_sum

        max_components = 0
        dfs(0, -1)  
        return max_components

        
