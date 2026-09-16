class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if lengths are different they cannot be isomorphic
        if len(s) != len(t):
            return False
        # store mapping from s to t
        map_s = {}
        # Store mapping from t to s
        map_t = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            # Check s to t mapping
            if c1 in map_s and map_s[c1] != c2:
                return False
            # Check t to s mapping
            if c2 in map_t and map_t[c2] != c1:
                return False
            # create the mappings
            map_s[c1] = c2
            map_t[c2] = c1
        return True
