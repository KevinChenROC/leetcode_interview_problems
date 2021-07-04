# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parentheses = []
        path = "("
        tried = {"(": True}
        l = n - 1
        r = n  ## l and r are # of left and right parentheses not used yet.

        while path:
            backtrack = False
            if (l > 0) and (path + "(" not in tried):
                tried[path + "("] = True
                path = path + "("
                l -= 1

            # num of left paran should be >= num of right paren + 1
            elif (r > 0) and (path + ")" not in tried) and n - l >= n - r + 1:
                tried[path + ")"] = True
                path = path + ")"
                r -= 1
            else:
                # reach dead end. Backtrack.
                backtrack = True

            if backtrack or l == r == 0:
                if l == r == 0 and path[-1] == ")":
                    parentheses.append(path)

                if path[-1] == ")":
                    r += 1
                elif path[-1] == "(":
                    l += 1
                path = path[0:-1]

        return parentheses


sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:
# 1 <= n <= 8
