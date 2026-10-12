class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        l=0
        for n in nums_set:
            if (n-1) not in nums_set:
                le=1
                while (n+le) in nums_set:
                    le+=1
                l = max(le,l)
        return l

