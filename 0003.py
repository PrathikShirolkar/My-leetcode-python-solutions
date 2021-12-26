class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_fragment_len = 0
        fragment_set = set()
        fragment = ""
        indx = 0
        prev = 0
        for i in s:
            fragment += i
            if i not in fragment_set:
                fragment_set.add(i)
            else:
                max_fragment_len = max(max_fragment_len,len(fragment_set))
                fragment_set -= set(fragment[prev:fragment.index(i)])
                fragment = fragment[fragment.index(i)+1:]
            indx +=1
        max_fragment_len = max(max_fragment_len, len(fragment_set))
        return max_fragment_len