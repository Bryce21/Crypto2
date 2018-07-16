if __name__ == "__main__":
    print("Point addition")
    # Fields
    mod = 67
    px = 2
    py = 22
    a = 0
    qx = 52
    qy = 7
    check = (qy - py) / (qx - px)
    print(check)
    if not float(check).is_integer():
        den_inv = pow(( (qx - px) ), mod - 2, mod)
        c = ((qy - py) * den_inv) % mod
    else:
        c = check % mod
    rx = (c ** 2 - px-qx) % mod
    ry = (c * (px - rx) - py) % mod
    print("C is: {}, rx/ry is: ({}, {})".format(c, rx, ry))


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
