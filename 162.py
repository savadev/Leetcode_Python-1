"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

"""




## O(N) Complexity
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums[0] ==max(nums):
            return 0
        if nums[len(nums)-1] == max(nums):
            return len(nums)-1
            
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                   return i
            
        return 0


## O(log(N)) Complexity

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
           left = 0
           right = len(nums) -1 
           self.binarySearch(nums, left, right)
        
    def binarySearch(self, nums, left, right):
           mid= (left+right)//2
           if left == right or nums[mid] > max(nums[mid-1],nums[mid+1]) :
                return mid
           return self.binarySearch(nums, left, mid-1 ) if nums[mid] > nums[mid+1] else self.binarySearch(nums, mid+1, right)
