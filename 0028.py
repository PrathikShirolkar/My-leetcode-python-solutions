class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif haystack == needle:
            return 0
        else:
            index = -1
            if len(needle) == 1:
                print(haystack)
                for i in range(len(haystack)):
                    if haystack[i] == needle:
                        index = i
                        break
            else:
                needle_len = len(needle)
                print(haystack[:-1*(needle_len-1)])
                for i in range(len(haystack[:-1*(needle_len-1)])):
                    if haystack[i:i+needle_len] == needle:
                        index = i
                        break
            return index
        