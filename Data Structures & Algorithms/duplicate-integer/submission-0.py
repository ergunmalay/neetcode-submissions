class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set([])

        for x in nums: # 1 , 2 , 3
            if x in hs:
                return(True)
            else:
                hs.add(x)
        return(False)
