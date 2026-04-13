class Solution:
    def findMin(self, nums: List[int]) -> int:

        # O(n) solution 
        # min = float('inf')
        # for n in nums:
        #     if n < min: min = n
        # return min

        # O(log n) solution
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]