
users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

usersDict = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}


whole_visits = len(users)
unique_users = set(users)
unique_visits = len(unique_users)
usersDict["Общее количество"] = whole_visits
usersDict["Уникальные посещения"] = unique_visits

print(usersDict)
