

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        mini = deque()
        maxi = deque()

        for r in range(len(nums)):
            while mini and nums[mini[-1]] > nums[r]:
                mini.pop()
            mini.append(r)
            
            while maxi and nums[maxi[-1]] < nums[r]:
                maxi.pop()
            maxi.append(r)
            
            while nums[maxi[0]] - nums[mini[0]] > 2:
                l += 1
                if maxi[0] < l:
                    maxi.popleft()
                if mini[0] < l:
                    mini.popleft()
            
            ans += r - l + 1

        return ans
