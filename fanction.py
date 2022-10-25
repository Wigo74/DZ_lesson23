import re
from typing import List, Any


def filter_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda x: param in x, data))


def map_query(param: int, data: List[str]) -> List[str]:
    return list(map(lambda x: x.split(' ')[param], data))


def unique_query(data: List[str], *args: Any, **kwargs) -> List[str]:
    return list(set(data))


def sort_query(data: List[str], param: str) -> List[str]:
    reverse: bool = False if param == 'asc' else True
    return list(sorted(data, reverse=reverse))


def limit_query(data: List[str], param: int) -> List[str]:
    limit: int = int(param)
    return list(data)[:limit]


def image_query(data: List[str], param: str) -> List[str]:
    regexp: re.Pattern = re.compile(param)
    return list(filter(lambda x: re.search(regexp, x), data))

