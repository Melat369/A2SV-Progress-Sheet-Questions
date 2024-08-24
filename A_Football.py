

def findTheWinner(n,goals):
    team_goals = {}
    for goal in goals:
        team = goal.strip()
        if team in team_goals:
            team_goals[team] += 1
        else:
            team_goals[team] = 1
    
    winner = max(team_goals, key=team_goals.get)
    return winner




n = int(input())
goals = [input() for _ in range(n)]

winner = findTheWinner(n,goals)
print(winner)