class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        return[key for key, value in sorted(d.items(), key=lambda item: item[1],reverse=True)[:k]]