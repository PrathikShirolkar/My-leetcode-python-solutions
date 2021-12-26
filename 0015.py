import math

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        else:
            freq = dict()
            for i in nums:
                if i not in freq.keys():
                    freq[i] = 0
                freq[i] +=1

            ret = set()
            set_nums = set(nums)
            n=len(freq)
            if  n>=3 :
                stop_pt = (math.factorial(n)/(math.factorial(n-3)*math.factorial(3)))+1
            else:
                stop_pt = 1
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j:
                        if len(ret)==stop_pt:
                            break
                        else:
                            ans = []
                            if -1*(nums[i]+nums[j]) in set_nums:
                                if -1*(nums[i]+nums[j]) in set([nums[i],nums[j]]):
                                    if nums[i]!=nums[j]:
                                        if freq[-1*(nums[i]+nums[j])]>1:
                                            ans = [nums[i],nums[j],-1*(nums[i]+nums[j])]
                                    else:
                                        if freq[-1*(nums[i]+nums[j])]>2:
                                            ans = [nums[i],nums[j],-1*(nums[i]+nums[j])]
                                else:
                                    ans = [nums[i],nums[j],-1*(nums[i]+nums[j])] 
                            else:
                                pass
                            ans.sort()
                            ans=tuple(ans)
                            if len(ans)>0 and ans not in ret:
                                ret.add(ans)
            return ret
                    
        

        