class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        if 2<= numRows:
            triangle.append([1,1])
        for i in range(2,numRows):
            temp = []
            for j in range(len(triangle[-1])-1):
                temp.append(triangle[-1][j]+triangle[-1][j+1])
            triangle.append([1]+temp+[1])
        return triangle