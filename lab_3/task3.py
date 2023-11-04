
def count_letters(text):
    text = text.lower()
    alph_dict = {}
    for char in text:
        if not char.isalpha():  # Если символ не является буквой - пропускаем итерацию
            continue

        if char in alph_dict:
            alph_dict[char] += 1  # Увеличиваем количество вхождений буквы в алфавит
        else:
            alph_dict[char] = 1  # Если буква не в алфавите, то добавляем её в алфавит

    return alph_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(count):
    frequency_dict = {}
    counts = count.values()
    whole_count = sum(counts)
    for char in count:
        frequency_dict[char] = round(count[char] / whole_count, 2)
    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letters_count = count_letters(main_str)
letters_frequency = calculate_frequency(letters_count)
# TODO Распечатайте в столбик букву и её частоту в тексте
for letter in letters_frequency:
    print(f"{letter}: {letters_frequency[letter]:.2f}")
