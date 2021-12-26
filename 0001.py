class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        ans = list()
        for i in nums:
            if target - i in s:
                if i != target - i: 
                    a = nums.index(i)
                    b = nums.index(target-i)
                    if a!=b:
                        ans.append(a)
                        ans.append(b)
                        break
                else:
                    a = nums.index(i)
                    temp_nums = nums [:a] + nums[a+1:]
                    temp_s = set(temp_nums)
                    print(i,temp_s)
                    if i in temp_s:
                        b = temp_nums.index(i)
                        b += 1
                        ans.append(a)
                        ans.append(b)
                        break
        return ans