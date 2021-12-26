class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) ->  float:
        temp = nums1 + nums2
        temp.sort()
        count = len(nums1) + len(nums2)
        half = int(count/2)
        if count%2 ==0:
            return (temp[half] + temp[half-1])/2
        else:
            return temp[half]