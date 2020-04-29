def prod(ln):
    prod = [0 for i in range(ln + 1)]
    prod[1] = 1

    for i in range(2, ln + 1):
        for j in range(1, (i // 2 + 1)):
            prod[i] = max(prod[i], j * (i - j) ,j * prod[i - j])

    return prod



if __name__ == '__main__':
    ln = int(input("length :"))
    print(prod(ln))