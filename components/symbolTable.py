class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def set(self, key, val):
        if key in self.symbols:
            self.symbols[key] = val
        else:
            raise ValueError(f"Cannot set value of undeclared variable '{key}'.")

    def get(self, key):
        if key in self.symbols:
            return self.symbols[key]
        else:
            raise ValueError(f"Tried to access inexistent variable '{key}'")

    def declare(self, key, val):
        self.symbols[key] = val

    def contains(self, key):
        if key in self.symbols:
            return True
        return False

    def dropReturn(self):
        del self.symbols["return"]
