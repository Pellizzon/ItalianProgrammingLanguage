import re


class PrePro:
    def __init__(self, initCode):
        self.code = initCode

    def filter(self):
        return re.sub(r"/\*.*?\*/", "", self.code)

    def check_PAR_balance(self):
        stack = []
        for i in self.code:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    raise ValueError("Found closing parenthesis, but stack was empty")
        if len(stack) != 0:
            raise ValueError("Code is unbalanced")