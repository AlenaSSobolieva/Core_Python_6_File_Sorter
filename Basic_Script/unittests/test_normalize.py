import unittest
from Basic_Script.normalize_file import name_normalize

class TestNormalize(unittest.TestCase):
    valid_cases = [
        ('мій_файл', 'mjej_fajl'),
        ('ВІДЕОФАЙЛ', 'VJEDEOFAJL'),
        ('МУЗИЧНИЙ КЛІП', 'MUZICHNIJ_KLJEP'),
        ('fixed tab', 'fixed_tab'),
        ('цікаве video', 'tsjekave_video'),
        ('Документ 345', 'Dokument_345'),
        ('swot-аналіз+висновок', 'swot_analjez_visnovok'),
        ('Файл! Назва@тест', 'Fajl__Nazva_test'),
        ('', ''),
        ('!@#$%^&*()_+{}[]|;:\'",.<>?/', '___________________________')
    ]
    invalid_cases = [
        (123, TypeError),
        (20.5, TypeError),
        (None, TypeError)
    ]

    def test_return_result(self):
        for words, result in self.valid_cases:
            result = name_normalize(words)
            self.assertEqual(result, result)

    def test_error(self):
        for a, ext_type in self.invalid_cases:
            with self.assertRaises(ext_type):
                name_normalize(a)

    if __name__ == '__main__':
        unittest.main()