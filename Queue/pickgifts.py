class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        for i in gifts:
            heappush(heap,-i)
        ans=0
        while k:
            ele=-heappop(heap)
            heappush(heap,- int(sqrt(ele)))
            k-=1
        
        return - sum(heap)

