class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        opened = ['(','{','[']
        closed = [')','}',']']
        for i in range(len(s)):
            if s[i] in opened:
                stack.append(s[i])
            elif s[i] in closed:
                if len(stack) == 0:
                    return False
                match s[i]:
                    case ')':
                        if stack[len(stack)-1] == '(':
                            stack.pop()
                        else:
                            return False
                    case '}':
                        if stack[len(stack)-1] == '{':
                            stack.pop()
                        else:
                            return False
                    case ']':
                        if stack[len(stack)-1] == '[':
                            stack.pop()
                        else:
                            return False
        return len(stack) == 0