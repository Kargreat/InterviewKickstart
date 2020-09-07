ip_ = 7


def max_product_from_cut_pieces(n):
    pieces = dict()
    pieces[0] = 1
    pieces[1] = 1
    pieces[2] = 2
    max_pieces = 1
    for i in range(3, n+1):
        for j in range(2, i):
            cur_pieces = pow(j, i // j) * pieces[i % j]
            if cur_pieces > max_pieces:
                max_pieces = cur_pieces
            print(cur_pieces)
        pieces[i] = max_pieces

    return pieces


if __name__ == '__main__':
    print(max_product_from_cut_pieces(ip_))
