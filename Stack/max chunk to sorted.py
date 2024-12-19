class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        c=0
        stack=[]

        for i in range(len(arr)):
            maxi=arr[i]

            while stack and stack[-1]>arr[i]:
                maxi=max(stack[-1],maxi)
                stack.pop()
            stack.append(maxi)
        return len(stack)

            
       
