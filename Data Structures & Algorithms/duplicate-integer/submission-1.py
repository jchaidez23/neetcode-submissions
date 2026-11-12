class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsD = {}
        for i in nums:
            if numsD.get(i) == 1:
                return True
            numsD[i] = 1
        return False
        