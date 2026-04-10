class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force big o notation O(n2)
        # mx = -1
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         distance = (j-i)
        #         water_level = min(heights[i],heights[j])
        #         calculate = distance * water_level
        #         if calculate > mx:
        #             mx = calculate
        # return mx
        #solve using : O(n)
        l = 0
        r = len(heights)-1 # O(1)
        mx = float('-inf')
        while l < r:
            distance = (r-l)
            water_level = min(heights[l],heights[r])
            calculate = distance * water_level
            if calculate > mx :
                mx = calculate
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return mx





        
