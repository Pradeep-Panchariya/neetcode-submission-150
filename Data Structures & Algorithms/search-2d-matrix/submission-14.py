class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows , cols = len(matrix),len(matrix[0])
        l = 0 
        r = (rows*cols)-1
        while l <= r:
            mid = (l+r)//2  

            rr = mid // cols
            cc = mid % cols

            mid_val = matrix[rr][cc]   
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid+1
            else:
                r = mid-1


        return False
        
        