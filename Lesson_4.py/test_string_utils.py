
from string_utils import StringUtils


import pytest
@pytest.mark.parametrize("string,expected_output", 
      [ ("skypro", "Skypro"),  # латиница (с маленькой)
        ("Skypro", "Skypro"), # латиница (уже с заглавной)
        ("hello world", "Hello world"),  # строка с пробелом
        ("123abc", "123abc"),  # строка с цифрами
        ("", ""),  # пустая строка
        ("Скайпро", "Скайпро"),  # кириллица (уже с заглавной)
        ("скайпро", "Скайпро"),  # кириллица (с маленькой)
        ("a", "A"),  # одна буква
      ]) 

def test_capitilize(string, expected_output):
   utils = StringUtils()
   result = utils.capitilize(string)
   assert result == expected_output


@pytest.mark.parametrize("string,expected_output",
         [(" space", "space"),# строка с пробелом )
          ("  space", "space"),# строка с двумя пробелами
          ("space", "space"), # без пробела 
          (" Hi, how are you?", "Hi, how are you?"),# несколько слов с пробелами            
          ("", ""), # пустая строка
          (" ", ""),# пустая строка с пробелом 
          ])                        
                                                                  
def test_trim(string, expected_output):
   utils_1 = StringUtils()
   result = utils_1.trim(string)
   assert result == expected_output


@pytest.mark.parametrize("string,delimiter,expected_output",
        [("a,b,c,d", ",", ["a", "b", "c", "d"]), #строка - список
         ("1:2:3", ":", ["1", "2", "3"]), # строка - список (цифры)
         ("первый/второй/третий", "/", ["первый", "второй", "третий"]), # слова делитель спецсимвол
         ("a b c", " ", ["a", "b", "c"]), # делитель пробел
         ("single", ",", ["single"]), # нет разделителя
         ("skypro,,skyeng", ",", ["skypro", "", "skyeng"]) # пустой элемент
        ] )

def test_to_list(string, delimiter, expected_output):
    utils_2 = StringUtils()
    result = utils_2.to_list(string, delimiter)
    assert result == expected_output


@pytest.mark.parametrize("string,symbol,expected_output",
        [("SkyPro", "S", True), # латиница заглавная 
         ("SkyPro", "o", True), # латиница последняя буква 
         ("Скайпро", "С", True), # кириллица заглавная
         ("Скайенг", "а", True), # кириллица нижний регистр
         ("123456", "1", True), # цыфры
         ("peace@labor@may", "@", True), # спецсимвол
         ("Peace", "", True), #пустой символ
         ("12345", "-1", False), # отрицательная цыфра 
         ("SkyPro", "p", False), # проверка регистра
         ("SkyPro", "Y", False), # проверка регистра
         ("Скайпро", "C", False), # C- латиница
         ("", "q", False) # пустая строка
         ])

def test_contains(string,symbol,expected_output):
    utils_3 = StringUtils()  
    result = utils_3.contains(string,symbol)
    assert result == expected_output

    # проверка когда первый аргумент "string" равен None
def test_string_is_none():
    utils_3 = StringUtils()
    with pytest.raises(AttributeError) as info:
        utils_3.contains(None, "a")
        assert "'no argument'" in str(info.value)


@pytest.mark.parametrize("string, symbol, expected_output",
        [("SkyPro", "k" , "SyPro"), # удаление одного символа
         ("SkyPro", "Pro", "Sky"), # удаление части слова
         ("Hello", "l", "Heo"), # Удаление двух символов
         ("Hello", "H", "ello"), #удаление первого символа
         ("Hello", "o", "Hell"), #удаление последнего символа
         ("Sky Pro", " ", "SkyPro"), # удаленике пробела
         ("8-999-123-45-67", "-", "89991234567"), # удаленике спецсимвола
         ("Победа", "По", "беда"), # кириллица
         ("SkyPro", "Eng", "SkyPro"), # отсутствие символа
         ("Hello", "Hello", "") # удаление всех символов
         ])



def test_delete_symbol(string,symbol,expected_output):
    utils_4 = StringUtils()
    result = utils_4.delete_symbol(string,symbol)
    assert result == expected_output


@pytest.mark.parametrize("string, symbol, expected_output",
      # Позитивные
      [("SkyPro", "S", True), #один символ
       ("SkyPro", "Sky", True), #несколько символов
       ("12345", "1", True), #цыыфры
       (" SkyPro", " ", True),#пробел
       ("", "", True), #пусто
       ("$£¢", "$", True), # проверка юникода
       # Негативные
       ("SkyPro", "P", False), # непервый символ
       ("Hello", "h", False), # проверка регистра
       ("SkyPro", "SkyE", False) #первые три символа совпадают следующий нет
       ])
def test_starts_with(string,symbol,expected_output):
    utils_5 = StringUtils()
    result = utils_5.starts_with(string,symbol)
    assert result == expected_output 

@pytest.mark.parametrize("string, symbol, expected_output",
      # Позитивные
      [("SkyPro", "o", True), # последний символ
      ("SkyPro", "Pro", True), #несколько символов в конце
      ("space ", " ", True), #пробел в конце
      ("12345", "5", True), # цифры
      ("", "", True), #пустота
      ("a", "a", True), # строка из одного символа
      ("符号", "号", True), # иероглифы 

      # Негативные
      ("SkyPro", "r", False), # предпоследний символ
      ("Text", "T", False), 
      ("eng", "weng", False)
      ])

def test_end_with(string,symbol,expected_output):
    utils_5 = StringUtils()   
    result = utils_5.end_with(string,symbol)
    assert result == expected_output


@pytest.mark.parametrize("string,expected_output", 
   # Позитивные
   [("", True),
    (" ", True),
    # Негативные
    ("SkyPro", False),
    (" SkyPro", False),
    ("123", False),
    ("!", False)
    ])   

def test_is_empty(string,expected_output):
    utils_6 = StringUtils()
    result = utils_6.is_empty(string)
    assert result == expected_output

@pytest.mark.parametrize("lst,joiner,expected_output",
        # Позитивные
        [([1,2,3,4,5,], ",", "1,2,3,4,5"),
         ([1.1,2.2,3.3,4.4,5.5,], ",", "1.1,2.2,3.3,4.4,5.5"),
         (["Sky", "Pro"], ",", "Sky,Pro"),
         (["Sky", "Pro"], "-", "Sky-Pro"),# разделитель не ','
         (["q", "w"], "", "qw"), # без разделителя
         ([], ",", ""), #пустой список
        ])    
def test_list_to_string(lst, joiner, expected_output):
    utils_6 = StringUtils()
    result = utils_6.list_to_string(lst,joiner)
    assert result == expected_output
# если значения None
def test_none_string():
        utils_6 = StringUtils()
        assert utils_6.list_to_string([None, None], "-") == "None-None"
        with pytest.raises(TypeError):
            utils_6.list_to_string(None) 