numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missing_item_idx = 4

normal_list = numbers[:missing_item_idx] + numbers[missing_item_idx + 1:]
sum_of_nums = sum(normal_list)
count_of_nums = len(numbers)

average = sum_of_nums / count_of_nums

numbers[missing_item_idx] = average

print("Измененный список:", numbers)
