class Solution:
    def isValid(self, s: str) -> bool:
        
        s_len = len(s)
        stack = []
        
        if(s_len % 2 != 0):
            return False
        
        for i in range(s_len):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) > 0 and s[i] == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
                elif len(stack) > 0 and s[i] == '}' and stack[len(stack)-1] == '{' and len(stack) > 0:
                    stack.pop()
                elif len(stack) > 0 and s[i] == ']' and stack[len(stack)-1] == '[' and len(stack) > 0:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False 