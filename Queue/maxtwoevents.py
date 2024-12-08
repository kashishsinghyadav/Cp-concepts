class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda event: event[1])        
        h = [(-event[2], event[0]) for event in events]
        heapq.heapify(h)
        ans = 0
        for start, end, value in events:
            while h and h[0][1] <= end:
                heapq.heappop(h)
            ans = max(ans, value - h[0][0] if h else value)
        return ans
