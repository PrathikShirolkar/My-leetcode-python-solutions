class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 1
        last_word = s.split(" ")[-1*i]
        i+i+1
        while len(last_word)==0:
            last_word = s.split(" ")[-1*i]
            i += 1

        return len(last_word)