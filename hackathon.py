hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
    return 'O ' + team_name + 'ficou classificada em ' + str(teams.index(team_name) + 1) + ' lugar'

get_score_1 = get_score("Team Ateliware", hackathon_1)
print(get_score_1)
# // A Team Ateliware ficou classificada em 2

get_score_2 = get_score("Team Kenzie", hackathon_1)
print(get_score_2)
# // A Team Kenzie ficou classificada em 1

get_score_3 = get_score("Team Mirum", hackathon_3)
print(get_score_3)
# // A Team Mirum ficou classificada em 1

# ok
# ok
# ok