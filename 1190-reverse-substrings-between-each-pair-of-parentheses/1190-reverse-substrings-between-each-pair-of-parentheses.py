class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = ""
        stack = []
        i = 0
        for ind, v in enumerate(s):
            if v == "(":
                stack.append(ind-i)
                print(stack)
                ans += v
            elif v == ")":
                temp = stack.pop()
                ans = ans[0:temp] + ans[temp+1:ind][::-1]
                i += 2
            else:
                ans += v
        return ans