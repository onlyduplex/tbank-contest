time = [int(f) for f in input().split()][1]
floors = [int(f) for f in input().split()]
leaver = int(input())
diffs = list()
for i in range(len(floors) - 1):
    diffs.append((floors[i] - floors[i + 1]) * -1)
lowers = diffs[:leaver - 1]
uppers = diffs[leaver - 1:]

if sum(lowers) < time or sum(uppers) < time:
    print(sum(diffs))
else:
    print(sum(min(lowers, uppers)) * 2 + sum(max(lowers, uppers)))
