"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        list = [item for item in range(1,n+1)]
        final = []
        for item in combinations(list,k):
            final.append(item)
        return final
