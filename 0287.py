class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        ret = -1
        for i in nums:
            if i in visited:
                ret = i
                break
            else:
                visited.add(i)
        return ret