# Funtion that returns the indices of two elemets.The sum of elements is equal to the targets

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(i==j):
                    continue
                else:
                    if((nums[i]+nums[j]) == target):
                        return i,j