class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        if len(s1)>len(s2):
            return False
        elif len(s1)==len(s2) and s1 == sorted(s2):
            return True
        for i in range(len(s2)-len(s1)+1):
            substr = sorted(s2[i:i+len(s1)])
            if substr == s1:
                return True
        return False