from django import template
from string import punctuation

register = template.Library()

PI_WORDS = (
    'редиска',
    'заголовок',
    'текст',
)


def clear_str(word: str) -> str:
    """Функция принимает str и возвращает str в нижнем регистре, но без символов перечисленных в punctuation."""
    ss = map(lambda x: x if x not in punctuation else "", word)
    result = ''.join(ss)
    return result.lower()


@register.filter()
def censor(value: str) -> str:
    """Фильтр проверяет переданный аргумент = ли он типу str или нет. Если нет, то выводится ошибка. Если да, то
    проходит проверка на наличие этого слов в картеже запрещённых, в случаи совпадения оно заменяется на *"""
    try:
        if type(value) == str:
            result = map(lambda word: '*' * len(word) if clear_str(word) in PI_WORDS else word, value.split())
            text = ' '.join(result)
        else:
            raise TypeError
    except TypeError as e:
        print(f'Необходимо передавать тип данных str, вместо этого получаем {type(value)}')
    else:
        return text


@register.filter()
def split(value: str, delimiter: str = '\n') -> list:
    """Фильтр преобразующий аргумент типа str в list для дальнейшего использования в цикле в html."""
    return value.split(delimiter)
