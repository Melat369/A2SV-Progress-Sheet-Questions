n = int(input())
skills = list(map(int, input().split()))

singers = []
dancers = []
actors = []

for i, skill in enumerate(skills):
    if skill == 1:
        singers.append(i+1)
    elif skill == 2:
        dancers.append(i+1)
    else:
        actors.append(i+1)

teams = min(len(singers), len(dancers), len(actors))
print(teams)

for i in range(teams):
    print(singers[i], dancers[i], actors[i])