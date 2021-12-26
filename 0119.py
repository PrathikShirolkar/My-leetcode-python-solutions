class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = [[1]]
        if 2<= rowIndex+1:
            triangle.append([1,1])
        for i in range(2,rowIndex+1):
            temp = []
            for j in range(len(triangle[-1])-1):
                temp.append(triangle[-1][j]+triangle[-1][j+1])
            triangle.append([1]+temp+[1])
        return triangle[-1]