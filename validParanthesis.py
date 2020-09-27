from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # go through the string
        
        # if (, [, { => push them to stack
        # if ), ], } => pop and compare
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
                new_char = stack.pop()
                
                if char == ')':
                    if new_char == '(':
                        continue
                    else:
                        return False
                if char == ']':
                    if new_char == '[':
                        continue
                    else:
                        return False
                
                if char == '}':
                    if new_char == '{':
                        continue
                    else:
                        return False
                else:
                    continue
                    
        if len(stack) != 0:
            return False
            
        return True
        