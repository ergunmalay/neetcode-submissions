class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            match = target - nums[i]

            if match in nums[i + 1:]:
                matchindex = nums.index(match, i + 1)
                print(i,matchindex)
                return[i,matchindex]