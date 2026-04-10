class Solution:
    def findMin(self, nums: List[int]) -> int:

        # O(n) solution 
        min = float('inf')
        for n in nums:
            if n < min: min = n
        return min
            
        