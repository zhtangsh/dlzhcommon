def order_book_id_in_group(order_book_id, group_size, group_id):
    """
    Calculate order_book_id in group

    :param order_book_id: stock unique id
    :param group_size:  group size
    :param group_id: group id
    :return:
    """
    number_part = order_book_id[:-5]
    return int(number_part) % int(group_size) == int(group_id)


def calculate_group(order_book_id_list, group_size, group_id):
    """
    Filter order_book_id from order_book_id_list with given group size & group id
    :param order_book_id_list: List of order_book_id
    :param group_size: group size
    :param group_id: group id
    :return:
    """
    res = []
    for order_book_id in order_book_id_list:
        ok = order_book_id_in_group(order_book_id, group_size, group_id)
        if not ok:
            continue
        res.append(order_book_id)
    return res


def number_in_group(number_part, group_size, group_id):
    """
    Determine whether given stock number is in the group
    :param number_part:  number part string
    :param group_size: group size
    :param group_id:  group id
    :return:
    """
    return int(number_part) % int(group_size) == int(group_id)
