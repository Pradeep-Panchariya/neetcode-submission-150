class Solution:
    def isValid(self, s: str) -> bool:

        matching_pair = {'{':'}','[':']','(':')'}
        stack = []
        for b in s:
            if b in matching_pair:
                stack.append(b)
            else:
                if stack:
                    opening = stack.pop() 
                    if matching_pair[opening] != b:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
        