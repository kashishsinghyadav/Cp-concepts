class Solution:
    def repeatLimitedString(self, s: str, re: int) -> str:
        fre_arr = [0] * 26

        for ch in s:
            fre_arr[ord(ch) - ord('a')] += 1

        i = 25
        ans = ''

        while i >= 0:
            if fre_arr[i] == 0:
                i -= 1
                continue

            count = min(re, fre_arr[i])
            ans += chr(i + ord('a')) * count
            fre_arr[i] -= count

            if fre_arr[i] > 0:
                j = i - 1
                while j >= 0 and fre_arr[j] == 0:
                    j -= 1
                if j < 0:
                    break
                ans += chr(j + ord('a'))
                fre_arr[j] -= 1

        return ans
