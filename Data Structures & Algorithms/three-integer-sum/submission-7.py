class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()

            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])

                if target in seen:
                    triplet.add((nums[i], target, nums[j]))

                seen.add(nums[j])

        return [list(t) for t in triplet]