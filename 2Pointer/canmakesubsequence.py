class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p1=0
        p2=0
        while p1<len(str1) and p2<len(str2):
            if str1[p1] == str2[p2] or chr((ord(str1[p1]) - ord('a') + 1) % 26 + ord('a')) == str2[p2]:
                p2+=1
            p1+=1
        if p2==len(str2):
            return True
        else:
            return False

            
