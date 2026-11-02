class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+": 
                stack.append(stack.pop() + stack.pop())  
            elif t == "-":
                sub = stack.pop()
                stack.append(stack.pop() - sub)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())            
            elif t == "/":
                divisor = stack.pop()
                stack.append(int(stack.pop() / divisor))
            else:
                stack.append(int(t))
                continue
            
        return stack[0]