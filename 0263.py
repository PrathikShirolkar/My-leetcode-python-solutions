class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        else:
            temp = n
            loop = 1
            ret = -1

            history = []
            while loop == 1:
                if temp%2 ==0:
                    temp = temp/2
                    history.append(2)
                    continue
                elif temp%3==0:
                    temp = temp/3
                    history.append(3)
                    continue
                elif temp%5==0:
                    temp = temp/5
                    history.append(5)
                    continue
                else:
                    if temp == 1:
                        ret = True
                    else:
                        ret = False
                    break
            print(history)
            print(ret)
            return ret