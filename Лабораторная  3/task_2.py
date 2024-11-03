# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    common = set(first_group.split(separator)).intersection(set(second_group.split(separator)))
    common_list = list(common)
    common_list.sort()
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator="|"))

