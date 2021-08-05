# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n=1 --> sum[0]
        # n=2 --> sum[1]

        sum = [1, 2]
        for i in range(2, n):
            sum.append(sum[i - 1] + sum[i - 2])

        return sum[n - 1]


sol = Solution()
print(sol.climbStairs(1))
print(sol.climbStairs(2))
print(sol.climbStairs(3))

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
