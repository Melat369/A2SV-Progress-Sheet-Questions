class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberstack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "/": lambda a, b: int(b / a),
            "*": lambda a, b: a * b
        }
        for i in tokens:
            if i in ops:
                numberstack.append(ops[i](numberstack.pop(), numberstack.pop()))
            else:
                numberstack.append(int(i))
        return numberstack[0]