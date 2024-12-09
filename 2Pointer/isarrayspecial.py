class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        m = len(queries)

        cum_sum = [0] * n
        cum_sum[0] = 0

        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                cum_sum[i] = cum_sum[i - 1] + 1
            else:
                cum_sum[i] = cum_sum[i - 1]

        result = [False] * m
        for i, query in enumerate(queries):
            start, end = query
            if cum_sum[end] - cum_sum[start] == 0:
                result[i] = True

        return result
