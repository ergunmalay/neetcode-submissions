class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs =  {}

        if len(s) != len(t):
            return(False)

        for x in s:
            hs[x] = hs.get(x,0) + 1
        
        for y in t:
            if y in hs.keys() and hs[y] != 0:
                hs[y] = hs.get(y) - 1
            else:
                return(False)
    
        return(True)


        