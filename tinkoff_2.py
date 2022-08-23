import collections

c = collections.Counter()
count_of_years = int(input())
teams  = []

for _ in range(count_of_years):
    team = input().split(' ')
    team.sort()
    team = ' '.join(team)
    c[team] += 1
print(c.most_common()[0][1])


