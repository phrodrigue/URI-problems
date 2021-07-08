while True:
    try:
        n = int(input())
        list = [int(x) for x in input().split()]
    except EOFError:
        break

    m = max(list)
    if m >= 20:
        print(3)
    elif m < 10:
        print(1)
    else:
        print(2)
