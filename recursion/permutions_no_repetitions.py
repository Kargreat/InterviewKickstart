ip_ = "thet"


def perm_with_no_repetitions(ipstr: str) -> list:
    op_ = list()
    partial_op_ = ""
    return helper(ip=ipstr, partial_op=partial_op_, op_=op_)


def helper(ip: str, partial_op: str, op_: list):
    if len(ip) == 0:
        op_.append(partial_op)
    else:
        for i in range(0, len(ip)):
            helper(ip[:i] + ip[i+1:], partial_op=partial_op + ip[i], op_= op_)
    return op_


if __name__ == '__main__':
    print(perm_with_no_repetitions(ip_))
    print(set(perm_with_no_repetitions(ip_)))