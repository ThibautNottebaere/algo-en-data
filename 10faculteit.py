def faculteit(n):
    # Basisgeval
    if n == 0 or n == 1:
        return 1
    else:
        # Recursieve stap
        return n * faculteit(n - 1)


# Hoofdprogramma
t = int(input())  # aantal testgevallen

for _ in range(t):
    n = int(input())  # lees elk getal in
    if n > 13:
        print("invoer te groot")
    else:
        print(faculteit(n))