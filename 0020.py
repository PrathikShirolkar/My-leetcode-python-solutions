class Solution(object):
    def reverse_sign(self, order):
        ret = ""
        for i in order:
            if i=="(":
                ret += ")"
            elif i=="{":
                ret += "}"
            elif i=="[":
                ret += "]"
        return ret
        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_map = {
            "(":"open",
            "{":"open",
            "[":"open",
            ")":"close",
            "}":"close",
            "]":"close",
        }
        
        open_order = ""
        close_order = ""
        
        if len(s)%2==0:
            err = False
            for i in s:
                #print(i)
                if par_map[i] == "open":
                    #print("    open")
                    open_order += i
                    close_order = self.reverse_sign(open_order[::-1])
                    #print("   "+str(open_order))
                    #print("   "+str(close_order))
                else:
                    #print("    close")
                    try:
                        if i == close_order[0]:
                            open_order = open_order[:-1]
                            close_order = self.reverse_sign(open_order[::-1])
                            #print("   "+str(open_order))
                            #print("   "+str(close_order))
                        else:
                            err = True
                            #print("    error")
                            break
                    except:
                        err = True
                        break
            #print("error",err)
            #print("open",open_order,len(open_order))
            if len(open_order)==0:
                return not err
            else:
                return False
        else:
            return False
        