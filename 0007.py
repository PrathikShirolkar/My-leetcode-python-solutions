class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x<0:
            ans = -1* int(str(x*-1)[::-1])
        else:
            ans = int(str(x)[::-1])
            
        if ans >= -2147483648 and ans<= 2147483647:
            return ans
        else:
            return 0