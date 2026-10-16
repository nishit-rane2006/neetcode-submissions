class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = re.sub(r'[^a-zA-Z0-9]', '', s)
        sc=sc.lower()
        i=0
        j=len(sc)-1
        while i<j:
            if sc[i] != sc[j]:
                return False
            else:
                i+=1
                j-=1
        return True