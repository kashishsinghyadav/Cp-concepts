class Solution:
    def getFinalState(self, nums: List[int], k: int, m: int) -> List[int]:
        
        h=[]
        for i in range(len(nums)):
            heappush(h,(nums[i],i))
        while k:
            ele,idx=heappop(h)
            heappush(h,(ele*m,idx))
            k-=1
        # print(h)
        while h:
            ele,idx=heappop(h)
            nums[idx]=ele
        return nums
