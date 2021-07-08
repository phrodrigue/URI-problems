while True:
    n = int(input())
    if n == -1:
        break
    print(n - 1 if n > 0 else n)