class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i,val in enumerate(s):
            if val in ['(', '{', '[']:
                stack.append(val)
            # otherwise its a closing and stack should exist
            elif stack:
                last = stack.pop()
                if val == ')' and last == '(':continue
                elif val == '}' and last ==  '{':continue
                elif val == ']' and last == '[':continue
                else: return False   
            else:
                return False
        if len(stack) == 0: return True
        return False


        