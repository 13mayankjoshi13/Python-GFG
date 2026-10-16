s = set(["a", "b", "c"])
print("Normal Set:", s)

fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)

Note: Frozensets are immutable, so methods like add() or remove() cannot be used. They are also hashable, which allows them to be used as dictionary keys.
