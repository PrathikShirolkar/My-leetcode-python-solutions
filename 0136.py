class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in nums:
            print(i)
            
            if i in s:
                s.discard(i)
            else:
                s.add(i)
        print(s)
        return list(s)[0]
        