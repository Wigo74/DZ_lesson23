from typing import Optional, List, Dict, Callable

import fanction

FILE_NAME = 'data/apache_logs.txt'

CMD_TO_FANCTION: Dict[str, Callable] = {
    "filter": fanction.filter_query,
    "map": fanction.map_query,
    "unique": fanction.unique_query,
    "sort": fanction.sort_query,
    "limit": fanction.limit_query,
    "image": fanction.image_query
}


def bild_query(cmd: str, param: str, data: Optional[List[str]]) -> List[str]:
    if not data:
        with open(FILE_NAME) as file:
            result: List[str] = list(map(lambda x: x.strip(), file))
    else:
        result = data

    return CMD_TO_FANCTION[cmd](param=param, data=result)
