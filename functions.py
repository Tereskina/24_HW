import re
from typing import Any


def filter_query(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda x: param in x, data))


def sort_query(param: str, data: list[str]) -> list[str]:
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def map_query(param: str, data: list[str]) -> list[str]:
    # отбирает колонку
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data: list[str], *args: Any, **kwargs: Any) -> list[str]:
    return list(set(data))


def limit_query(param: str, data: list[str]) -> list[str]:
    limit = int(param)
    return list(data)[:limit]


def regex_query(param: str, data: list[str]) -> list[str]:
    pattern: re.Pattern = re.compile(param)
    return list(filter(lambda x: re.search(pattern, x), data))
