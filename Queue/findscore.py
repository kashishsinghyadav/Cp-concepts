class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap=[]
        s=set()
        for i in range(len(nums)):
            heappush(heap,(nums[i],i))
        ans=0
        while heap:
            mini,idx=heappop(heap)
            if idx in s:
                continue
            print(mini)
            ans+=mini
            print(ans)
            if idx-1>=0:
                s.add(idx-1)
            if idx+1<len(nums):
                s.add(idx+1)
        return ans


                
