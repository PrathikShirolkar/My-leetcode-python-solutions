class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [i for i in str(num)]
        print(num)
        while len(num) !=1:
            num = [j for j in str(sum([int(i) for i in num]))]
        return num[0]
        