def transform(arr):
    result = []
    for i, e in enumerate(arr):
        result.append((-1)**(i + 1 - 1) * abs(e))
    return result



n = int(input())

subs = list(map(int, input().split(' ')))
subs = transform(subs)

min_pos = min(list(filter(lambda x: x > 0, subs)))
index_min_pos = subs.index(min_pos)


max_neg = min(list(filter(lambda x: x < 0, subs)))
index_max_neg = subs.index(max_neg)


subs[index_min_pos], subs[index_max_neg] = subs[index_max_neg], subs[index_min_pos]
print(sum(transform(subs)))


