
from string_utils import StringUtils


import pytest
@pytest.mark.parametrize("string,expected_output", 
      [ ("skypro", "Skypro"),  # обычная строка
        ("hello world", "Hello world"),  # строка с пробелом
        ("123abc", "123abc"),  # строка с цифрами
        ("", ""),  # пустая строка
        ("Скайпро", "Скайпро"),  # кириллица (уже с заглавной)
        ("скайпро", "Скайпро"),  # кириллица (с маленькой)
        ("a", "A"),  # одна буква
        (" space", " space")# строка с пробелом в начале
      ]) 

def test_capitilize(string, expected_output):
   utils = StringUtils()
   result = utils.capitilize(string)
   assert result == expected_output


