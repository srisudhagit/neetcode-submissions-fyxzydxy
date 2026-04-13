class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranMap = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if char in paranMap:
                stack.append(char)
            else:
                if stack and paranMap.get(stack[-1]) == char:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

        