n = int(input())
T = [int(x) for x in input().split()]

print(T.index(min(T)) + 1)