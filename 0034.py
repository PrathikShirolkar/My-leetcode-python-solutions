class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start_ind, end_ind = -1, -1
        
        rev_nums = nums[::-1]
        
        try:
            start_ind =  nums.index(target)
            end_ind =  rev_nums.index(target)
        except:
            print("exception")
            start_ind, end_ind = -1, -1
            return [-1,-1]
        return [start_ind, len(nums)-end_ind-1]