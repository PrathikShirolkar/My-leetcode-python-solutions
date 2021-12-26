class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 0:
            seed = strs[0]

            prefix = ""
            flag = 0
            for i in range(len(seed)):
                for j in strs[1:]:
                    try:
                        if seed[i] != j[i]:   
                            flag=-1
                            break
                    except:
                        flag=-1
                        break
                if flag==0:
                    prefix += seed[i]
                else:
                    break
            return prefix
        else:
            return ""