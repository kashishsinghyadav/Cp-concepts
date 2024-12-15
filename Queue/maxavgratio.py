class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n=len(classes)
        h=[]
        for p,t in classes:
            heapq.heappush(h,(-(((p+1)/(t+1))-(p/t)),p,t))
        for i in range(extraStudents):
            avg,p,t=heapq.heappop(h)
            p+=1
            t+=1
            heapq.heappush(h,(-(((p+1)/(t+1))-(p/t)),p,t))
        total = 0.0
        for i,p,t in h:
            total+=(p/t)
        return total/n
