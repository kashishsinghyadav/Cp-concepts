class Solution:
    def maximumLength(self, s: str) -> int:
        L = defaultdict(lambda: defaultdict(int))
        l = 0
        p = -1
        
        for c in s:
            l = l + 1 if c == p else 1
            p = c
            L[c][l] += 1
        
        res = -1
        
        for c in L.keys():
            max_length = max(L[c].keys())
            count = 3 
            for length in range(max_length, 0, -1):
                count -= L[c][length]
                if count <= 0:
                    res = max(res, length)
                    break
        
        return res
