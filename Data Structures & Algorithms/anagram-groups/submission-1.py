class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for i in strs:
            c = "".join(sorted(i))
            anagrams[c].append(i)

        return list(anagrams.values())
        