class Solution:
    def letterCombinations(self, dig: str) -> List[str]:
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        if dig=="":
            return []
        res=[]
        def solve(idx,st):
            nonlocal res
            if idx==len(dig):
                res.append(st)
                return
            char=d[dig[idx]]
            for i in char:
                st+=i
                solve(idx+1,st)
                st=st[:-1]
        solve(0,'')
        return res
