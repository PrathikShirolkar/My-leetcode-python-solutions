class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        larger_flag = 0
        last_ind = -1
        for ind in range(len(nums)):
            if  nums[ind] >= target:
                larger_flag = 1
                last_ind = ind
                break
        if last_ind == -1:
            return len(nums)
        else:
            return last_ind