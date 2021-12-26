class Solution:
    def myAtoi(self, str: str) -> int:
        temp = ""
        initial = 0
        write = 0
        sign = 0
        for i in str:
            if initial == 0 and i == ' ':
                pass
            else:
                if (i == "+" or i == "-" or i.isdigit() or i[1:].isdigit()) and (write == 0 or write == 1) and (sign==0 or sign ==1):
                    if(i == "+" or i == "-"):
                        if sign==0 and initial ==0:
                            sign += 1
                        else:
                            sign +=3
                    write = 1
                    if sign<2:
                        temp += i
                    initial = 1
                else:
                    write =2
        print(temp)
        if temp.isdigit() or temp[1:].isdigit():
            ans = int(temp)
            if ans > (2**31)-1:
                return (2**31)-1
            elif ans < -1*(2**31):
                return -1*(2**31)
            else:
                return ans
                
        else:
            return 0