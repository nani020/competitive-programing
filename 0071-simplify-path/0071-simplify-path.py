class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitted = path.split("/")

        print(splitted)
        for i in splitted:
         

            if i == "." or i == "":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
                continue
            else:
                stack.append( "/"+i)
        if stack:
            return "".join(stack)
        return "/"