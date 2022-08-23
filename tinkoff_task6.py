def find(arr, cond, value):
    for el in arr:
        if cond(value, el):
            return el
    return None

def condition(lhs, rhs):
    return lhs[1] == rhs[0]


n = int(input())

count = 0
floors = []
for _ in range(n):
    start, finish = map(int, input().split(' '))
    floors.append((start, finish))

floors = sorted(floors, key=lambda x: x[0] and x[1])

min_floor = floors[0]
floors.remove(min_floor)
count += 1

while True:
    first = find(floors, condition, min_floor)
    if first:
        count +=1
        min_floor = first
        floors.remove(min_floor)
    else:
        break
print(count)
