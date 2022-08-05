class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i == '[' or i=='{':
                stack.append(i)
            else:
                if not bool(stack):
                    return False
                elif i ==']':
                    if stack[-1]=='[':
                            stack.pop()
                    else:
                        return False
                elif i==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                            return False
                else:
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
        if bool(stack):
            return False
        return True

        