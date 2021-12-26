class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) > 1:
            max_len = 0
            max_string = ""
            for ind in range(len(s)):
                for i in range(len(s[ind:])+1): 
                    if ind != ind+i:
                        if s[ind:ind+i] == s[ind:ind+i][::-1]:
                            if max_len < len(s[ind:ind+i]):
                                max_string = s[ind:ind+i]
                                max_len = len(s[ind:ind+i])
            return max_string
        else:
            return s