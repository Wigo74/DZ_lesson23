import fanction

FILE_NAME = 'data/apache_logs.txt'

CMD_TO_FANCTION = {
    "filter": fanction.filter_query,
    "map": fanction.map_query,
    "unique": fanction.unique_query,
    "sort": fanction.sort_query,
    "limit": fanction.limit_query
}


def bild_query(cmd, param, data):
    if not data:
        with open(FILE_NAME) as file:
            result = list(map(lambda x: x.strip(), file))
    else:
        result = data

    return CMD_TO_FANCTION[cmd](param=param, data=result)



