class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for i,v in enumerate(numbers):
            match = target - v
            if v in seen:
                continue
            
            if match in numbers[i + 1:]:
                matchindex = numbers.index(match, i + 1)
                print(matchindex)
                return([i+1,matchindex+1])
            else:
                seen.add(v)