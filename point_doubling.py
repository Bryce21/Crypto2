
def point_doubling(mod, a, px, py):
    check = ((3 * px ** 2) + a) / (2 * py)
    # print(check)
    if not float(check).is_integer():
        den_inv = pow((2 * py), mod - 2, mod)
        c = (((3 * px ** 2) + a) * den_inv) % mod
        # print(c)
    else:
        c = (((3 * px ** 2) + a) / (2 * py)) % mod
    rx = (c ** 2 - (2 * px)) % mod
    ry = (c * (px - rx) - py) % mod
    print("C is: {}, rx/ry is: ({}, {})".format(c, rx, ry))

def main():
    z = 17  # int(input("Please enter the data value: "))  # Data number #17
    mod = 67  # int(input("Please enter the module divisor you would like to use: "))  # order #67
    n = 79  # int(input("Please enter the order: "))  # order #79
    d = 2  # int(input("Please enter the private Key: "))  # private key #2
    a = 0  # int(input("Please enter the value for a: "))  # intercept ellipse equation #0
    px = 25  # int(input("Please enter the x coordinate of the base point: "))  # base point x point #2
    py = 17  # int(input("Please enter the y coordinate of the base point: "))  # base point y point #22

    point_doubling(mod, a, px, py)


if __name__ == "__main__":
    main()
