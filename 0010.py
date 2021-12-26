class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        try:
            x = re.search(p, s)
            if x.group() == s:
                return True
            else:
                return False
        except:
            return False