def matematyczna_reszta(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez 0!")
    return ((a % b) + abs(b)) % abs(b)

print(matematyczna_reszta(-14,3))