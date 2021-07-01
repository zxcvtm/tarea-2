nTeamsResponses = int(input()
teamsResponses = list()
for i in range(nTeamsResponses):
    t = input()
    teamsResponses.append(t)
teams = set(teamsResponses)
for team in teams:
    if teamsResponses.count(team) > 1:
        print(team)
