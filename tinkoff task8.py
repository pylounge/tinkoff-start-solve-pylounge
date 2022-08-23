import re

inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])

domains = []
clients = []

for _ in range(n):
    domains.append(input())

for _ in range(m):
    clients.append(input())

for req in clients:
    first_part, second_part = req.split(' ')
    reg_exp = fr"{first_part}(.)+{second_part}"
    print(len(list(filter(lambda x: re.search(reg_exp, x),domains))))
