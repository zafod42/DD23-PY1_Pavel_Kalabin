list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_of_teams = 2

listSize = len(list_players)
teamSize = listSize // number_of_teams
team1 = list_players[:teamSize]         # Подразумевается [0:teamSize] при слайсировании
team2 = list_players[teamSize:]
print(team1)
print(team2)
