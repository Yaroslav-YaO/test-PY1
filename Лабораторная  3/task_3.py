



# TODO Напишите функцию calculate_frequency


def count_letters(str_):
    uniq_letter = {}
    lower_str_ = str_.lower()
    for letter in lower_str_:
        if letter.isalpha():
            if letter in uniq_letter:
                uniq_letter[letter] += 1
            else:
                uniq_letter[letter] = 1
    return uniq_letter

def calculate_frequency(dict_letter):
    sum_letter = 0
    for key in dict_letter:
        sum_letter += dict_letter[key]
    for key in dict_letter:
        dict_letter[key] /= sum_letter

    return dict_letter



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

dict_letter = count_letters(main_str)
new_dict_letter = calculate_frequency(dict_letter)

for key in new_dict_letter:
    print(f"{key}: {new_dict_letter[key]:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте