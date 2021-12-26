class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = -1
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                ret = i
                break
        return ret
        