class Solution(object):
    
    def romanToInt(self, s):
        conversion = {"I" : 1,
                      "V" : 5,
                      "X" : 10,
                      "L" : 50,
                      "C" : 100,
                      "D" : 500,
                      "M" : 100}
        output = 0
        for ind in range(len(s)):
            if s[ind] == "I":
                if ind+1 < len(s):
                    output += (-1 if (s[ind+1]=="V" or s[ind+1]=="X") else 1)
                else:
                    output += 1
            elif s[ind] == "X":
                if ind+1 < len(s):
                    output += -10 if (s[ind+1]=="L" or s[ind+1]=="C") else 10
                else:
                    output += 10
            elif s[ind] == "C":
                if ind+1 < len(s):
                    output += -100 if (s[ind+1]=="D" or s[ind+1]=="M") else 100
                else:
                    output += 100
            elif s[ind] == "V":
                output += 5
            elif s[ind] == "L":
                output += 50
            elif s[ind] == "D":
                output += 500
            elif s[ind] == "M":
                output += 1000
        return output
            
            
                
        