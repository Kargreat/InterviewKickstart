ip_ = 3


def generate_subsets(n, partial_op_, op_):
    if n == 0:
        op_.append(partial_op_)
    else:
        partial_op_ = partial_op_ + str(n)
        generate_subsets(n=n-1, partial_op_=partial_op_, op_=op_)
        partial_op_ = partial_op_[:-1]
        generate_subsets(n=n-1, partial_op_=partial_op_, op_=op_)
    return op_


def subsets(n: int):
    partial_op_ = ""
    op_ = []
    op_ = generate_subsets(n, partial_op_, op_)
    return op_


if __name__ == '__main__':
    print(subsets(ip_))