def _get_arr(key, val=None):
    arg = ([], [val])[val is not None]
    return (tuple, list)[key](arg)


def map(cb, arr):
    argcount = cb.__code__.co_argcount
    is_list = type(arr) is list
    temp = _get_arr(is_list)

    for idx, item in enumerate(arr):
        arg_list = (item, idx, arr)[:argcount]
        res = cb(*arg_list)
        temp += _get_arr(is_list, res)

    return temp


def filter(cb, arr):
    argcount = cb.__code__.co_argcount
    is_list = type(arr) is list
    temp = _get_arr(is_list)

    for idx, item in enumerate(arr):
        arg_list = (item, idx, arr)[:argcount]
        if cb(*arg_list):
            temp += _get_arr(is_list, item)

    return temp


def reduce(cb, arr, initial):
    argcount = cb.__code__.co_argcount
    temp = initial

    for idx, item in enumerate(arr):
        arg_list = (temp, item, idx, arr)[:argcount]
        temp = cb(*arg_list)

    return temp
