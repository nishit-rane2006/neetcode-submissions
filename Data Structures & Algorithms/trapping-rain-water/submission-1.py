class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0, len(height)-1
        l_m,r_m = height[l],height[r]
        w=0
        while l<r:
            if l_m<r_m:
                l+=1
                l_m = max(l_m,height[l])
                w += l_m - height[l]
            else:
                r-=1
                r_m = max(r_m, height[r])
                w += r_m - height[r]
        return w

            
        