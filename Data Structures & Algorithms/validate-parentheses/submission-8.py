class Solution:
    def isValid(self, s: str) -> bool:
        brackets_open = []

        for char in s:
            if char in ['(','{', '[']:
                brackets_open.append(char)
            elif char == ')':
                if not brackets_open or  brackets_open.pop() != '(':
                    return False
            elif char == '}':
                if not brackets_open or brackets_open.pop() != '{':
                    return False
            elif char == ']':
                if not brackets_open or brackets_open.pop() != '[':
                    return False

        return not brackets_open