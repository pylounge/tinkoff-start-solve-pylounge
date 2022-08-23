import re

inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])

workers = []
requests = []

for _ in range(n):
    workers.append(input())

for _ in range(m):
    req = input().split(' ')
    requests.append((int(req[0]),req[1]))


for request in requests:
    k, prefix = request
    workers_with_prefix = list(filter(lambda x: re.match(prefix, x), workers))
    workers_with_prefix.sort()
    if k <= len(workers_with_prefix):
        print(workers.index(workers_with_prefix[k - 1]) + 1)
    else:
        print(-1)

