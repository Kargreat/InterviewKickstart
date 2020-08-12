ip_ = 2


def decimal_numbers(n: int, partial_op: str):
    if n == 0:
        print(partial_op)
    else:
        initial_n = n
        for i in range(0, 10):
            partial_op = partial_op + str(i)
            decimal_numbers(n - 1, partial_op)
            partial_op = partial_op[:-1]


def generate_dec_nums(n):
    holder = ""
    decimal_numbers(n, holder)


if __name__ == '__main__':
    generate_dec_nums(ip_)
