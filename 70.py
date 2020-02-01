"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
              return n
        dp = [0 for ele in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        self.helper(dp , n)
        return dp[n]

    def helper(self, dp , k):
        if k>2 :
           if dp[k-1]==0 or dp[k-2]==0: 
              dp[k] = self.helper(dp, k-1)+ self.helper(dp, k -2)
           else:
              dp[k] = dp[k-1]+dp[k-2] 
           return dp[k]
        else:
            return dp[k]