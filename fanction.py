def filter_query(param, data):
    return list(filter(lambda x: param in x, data))


def map_query(param: int, data):
    return list(map(lambda x: x.split(' ')[param], data))


def unique_query(data, param=None):
    return list(set(data))


def sort_query(data, param):
    reverse = False if param == 'asc' else 'desc'
    return list(sorted(data, reverse=reverse))


def limit_query(data, param):
    limit = int(param)
    return list(data)[:limit]
