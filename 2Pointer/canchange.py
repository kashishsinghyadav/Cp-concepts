class Solution:
    def canChange(self, s: str, t: str) -> bool:
        if s.replace('_','') != t.replace('_',''):
            return False

        ls=[]
        ls = [(char, i) for i, char in enumerate(s) if char in "LR"]
        lt = [(char, i) for i, char in enumerate(t) if char in "LR"]
        for i,j in zip(ls,lt):
            if i[0]!=j[0]:
                return False

            if i[0]=='L' and i[1]<j[1]:
                return False
            if i[0]=='R' and i[1]>j[1]:
                return False
        return True

        
