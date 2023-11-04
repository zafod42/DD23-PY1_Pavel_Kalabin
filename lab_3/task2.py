# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    participants_first = first_group.split(separator)
    participants_second = second_group.split(separator)
    unique_part_first = set(participants_first)
    common_participants = list(set.intersection(unique_part_first, participants_second))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
