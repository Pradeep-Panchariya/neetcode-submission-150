class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #brute force big o notation O(n2)
        mx = -1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                distance = (j-i)
                water_level = min(heights[i],heights[j])
                calculate = distance * water_level
                if calculate > mx:
                    mx = calculate
        return mx


        
        # mx = float('-inf')
        # scnd_mx = float('-inf')
        # l = 0 
        # r = len(heights)
        # res = heights[r-1]
        # final = -1
        # while l < r:
        #     if heights[l] > mx :
        #         mx = heights[l]
        #         index = l 
        #     if res > scnd_mx:
        #         scnd_mx = res
        #         r-=1
        #     ans =(r - index)* min(scnd_mx,mx)
        #     if ans > final:
        #         final = ans
               
        #     l += 1
      
        # return final 





            


            
