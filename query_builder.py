from typing import Callable

import functions

CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': functions.filter_query,
    'sort': functions.sort_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'limit': functions.limit_query,
    'regex': functions.regex_query
}

FILE_NAME: str = 'data/apache_logs.txt'


def build_query(cmd1: str, value1: str, cmd2: str, value2: str) -> list[str]:

    with open(FILE_NAME) as file:
        prepared_data = list(map(lambda x: x.strip(), file))


    result_after_cmd1 = CMD_TO_FUNCTION[cmd1](param=value1, data=prepared_data)

    return CMD_TO_FUNCTION[cmd2](param=value2, data=result_after_cmd1)


