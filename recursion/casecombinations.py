from operator import itemgetter

ip_ = "ab"
op_ = ["t1D1", "T1D1", "t1d1", "t1D1"]


def case_combinations(iplist: str) -> list:
    """

    :type iplist: str
    """
    op_ = list()
    add_combinations(ip_list=iplist, combination="", partial_op=op_)
    return op_


def add_combinations(ip_list: str, partial_op: list, combination: str):
    if len(ip_list) == 0:
        partial_op.append(combination)
        combination = ""
    else:
        first_letter = ip_list[0]
        if not str.isdigit(first_letter):
            add_combinations(ip_list=ip_list[1:], combination=combination + str.lower(first_letter), partial_op=partial_op)
            add_combinations(ip_list=ip_list[1:], combination=combination + str.upper(first_letter), partial_op=partial_op)
        else:
            add_combinations(ip_list=ip_list[1:], combination=combination + str(first_letter), partial_op=partial_op)


if __name__ == '__main__':
    # print(case_combinations(ip_))
    a = [i for i in range(0,11)]
    