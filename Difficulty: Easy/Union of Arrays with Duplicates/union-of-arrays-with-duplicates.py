class Solution:    
    def findUnion(self, a, b):
        a = set(a)
        b= set(b)
        return set(a.union(b))