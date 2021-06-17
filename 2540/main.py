while True:
    try:
        n = int(input())
    except EOFError:
        break

    votos = list(map(int, input().split()))
    aFavor = votos.count(1)

    if aFavor >= n * 2 / 3:
        print("impeachment")
    else:
        print("acusacao arquivada")
