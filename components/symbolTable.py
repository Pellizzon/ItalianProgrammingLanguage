class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def set(self, key, val):
        self.symbols[key] = val

    def get(self, key):
        if key in self.symbols:
            return self.symbols[key]
        else:
            raise ValueError(f"Tried to access inexistent variable '{key}'")
