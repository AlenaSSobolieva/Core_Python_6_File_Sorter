# normalize_file.py

import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
LATIN_SYMBOLS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
TRANSLITERATION = {}

for cs, ls in zip(CYRILLIC_SYMBOLS, LATIN_SYMBOLS):
    TRANSLITERATION[ord(cs)] = ls # for small leters
    TRANSLITERATION[ord(cs.upper())] = ls.upper() # for capital letters


def name_normalize(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("Input must be a string.")

    transliterated_name = name.translate(TRANSLITERATION)

    if not isinstance(transliterated_name, str):
        raise TypeError("Translation result must be a string.")

    transliterated_name = re.sub(r'_+', '_', transliterated_name)

    return transliterated_name


# print(normalize('всі файли'))
# print(normalize_title('структуру і зміст'))

if __name__ == '__main__':
    pass
    # result = name_normalize('abc')
    # print(result)


