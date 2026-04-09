class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(NLogN)
        
        for i in range(len(nums)): #O(N)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = len(nums)-1 # O(1)
            while L < R:
                three_sum = nums[L]+nums[R]+nums[i]

                if three_sum > 0 :
                    R -= 1
                elif three_sum < 0 :
                    L += 1
                else:
                    res.append([nums[i],nums[L],nums[R]])
                    L+=1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return res


