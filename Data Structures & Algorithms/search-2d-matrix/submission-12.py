class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for index, mat in  enumerate(matrix):
            l = 0
            r = len(mat)-1
            print(mat)
            while l <= r:
                print(l,r)
                mid = (l+r)//2
                print(mid)
                if mat[mid] == target:
                    return True
                elif mat[mid] < target:
                    l = mid+1
                else:
                    r = mid-1


        return False
        
        