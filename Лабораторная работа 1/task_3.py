list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


mid_index = len(list_players) // 2 # делим игроков поровну на 2 команды

first = list_players[:mid_index] # c первого по третий
second = list_players[mid_index:] # с третьего по последний

print(first)
print(second)
