class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        curr = 0
        count = 0
        
        for i in range(1, n + 1):
            if i not in s and curr + i <= maxSum:
                curr += i
                count += 1
            elif curr + i > maxSum:
                break
        
        return count
