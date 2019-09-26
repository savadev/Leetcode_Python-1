"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = [[]]
        return self.helper(nums,final)
        
        
    def helper(self, sub_list, final) :
        print(final, sub_list)
        if len(sub_list) == 1 :             
              return [[]]+[sub_list]
        temp=[[]]
        for i in range(len(sub_list)):
               temp+= ([sorted( element+ [sub_list[i]]) for element in self.helper(sub_list[:i]+sub_list[i+1:], final) if  sorted(element+ [sub_list[i]]) not in temp])
               
        final = temp
        return final
        