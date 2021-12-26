class Solution(object):
    def mult(self, res, char_list):
        t_res = []
        if len(res) == 0:
            t_res = char_list
        else:
            for i in res:
                for j in char_list:
                    t_res.append(i+j)
        return t_res
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numMap = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        
        res = []
        for digit in digits:
            res = self.mult(res, numMap[digit])
        return res
        