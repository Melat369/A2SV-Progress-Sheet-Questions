t = int(input())
priority = {
    "rat": 1,
    "woman": 2,
    "child": 2,
    "man": 3,
    "captain": 4
}

people = []
for _ in range(t):
    name, status = input().split()
    people.append((name, priority[status]))

people.sort(key=lambda x: x[1])

for name, _ in people:
    print(name)