if __name__ == "__main__":
    print("Point doubling")
    # Fields
    mod = 67
    px = 2
    py = 22
    a = 0
    check = ((3 * px ** 2) + a) / (2 * py)
    print(check)
    if not float(check).is_integer():
        den_inv = pow((2 * py), mod - 2, mod)
        c = (((3 * px ** 2) + a) * den_inv) % mod
    else:
        c = (((3 * px ** 2) + a) / (2 * py)) % mod
    rx = (c ** 2 - (2 * px)) % mod
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