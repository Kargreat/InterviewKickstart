ip_ = 3


def generate_valid_parenthesis(n, open_p, close_p, partial_op, op_):
    if open_p == close_p == 0:
        op_.append(partial_op)
        partial_op = ""
    if close_p < open_p:
        partial_op = ""

    if open_p > 0:

        partial_op = partial_op + "{"
        open_p -= 1
        generate_valid_parenthesis(n, open_p, close_p, partial_op, op_)

    if close_p > 0:
        partial_op = partial_op + "}"
        close_p -= 1
        generate_valid_parenthesis(n, open_p, close_p, partial_op, op_)

    return op_


def valid_parenthesis(n: int):
    open_p = close_p = n
    op_ = []
    partial_op = ""
    op_ = generate_valid_parenthesis(n, open_p, close_p, partial_op, op_)
    return op_


if __name__ == '__main__':
    print(list(set(valid_parenthesis(ip_))))