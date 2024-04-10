n = int(input())
print(*sorted(list(map(int, input().split())), key=lambda x: x % 10))
