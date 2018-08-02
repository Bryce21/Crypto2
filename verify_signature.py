import random
import sys


def point_doubling(mod, a, px, py):
    check = ((3 * px ** 2) + a) / (2 * py)
    # print(check)
    if not float(
            check).is_integer():  # checking to see if NOT an integer ie a fraction and you need to find the mod inverse
        den_inv = pow((2 * py), mod - 2, mod)
        c = (((3 * px ** 2) + a) * den_inv) % mod
        # print(c)
    else:
        c = ((3 * px ** 2) + a) % mod
    new_rx = (c ** 2 - (2 * px)) % mod
    new_ry = (c * (px - new_rx) - py) % mod
    return {"rx": new_rx, "ry": new_ry}


def point_addition(mod, a, px, py, qx, qy):
    check = (qy - py) / (qx - px)

    if not float(check).is_integer():
        den_inv = pow((qx - px), mod - 2, mod)
        c = ((qy - py) * den_inv) % mod
    else:
        c = check % mod

    new_rx = (c ** 2 - px - qx) % mod
    new_ry = (c * (px - new_rx) - py) % mod
    return {"rx": new_rx, "ry": new_ry}

def var_sig_pair_uv(mod, k, px, py, a):
    # These will be overwritten multiple times, and initially should be the first point
    rx = px
    ry = py

    # When converting a float to an int, python automatically rounds a decimal down.
    num_multiplication = int(k / 2)

    # Each time a doubling is done, replace the current point with the newly calculated value
    for i in range(num_multiplication):
        doubling_result = point_doubling(mod, a, rx, ry)
        rx = doubling_result["rx"]
        ry = doubling_result["ry"]

    # Only need to add points when k >= 3 and is odd. In other cases, doubling will be enough
    if (k % 2 == 1) and k > 2:
        addition_result = point_addition(mod, a, px, py, rx, ry)
        rx = addition_result["rx"]
        ry = addition_result["ry"]


def verify_sig_pair(r, s, n, qqx, qqy, z, a, px, py):
    #qqx = int(input("Please enter the x coordinate of the public key: "))  # public key x point #52
    #qqy = int(input("Please enter the y coordinate of the public key: "))  # public key y point #7

    if not 1 <= r < (n - 1):
        print("r is not between 1 and n-1")
        sys.exit()
    elif not 1 <= s < (n - 1):
        print("s is not between 1 and n-1")
        sys.exit()
    else:
        # print check to see if can get to this statement
        # print("success {} {}".format(qqx, qqy))
        s_inv = pow(s, n - 2, n)
        w = s_inv % n
        u = (z * w) % n
        v = (r * w) % n

        var_sig_pair_uv(n, u, px, py, a)
        ugx = rx #error here with these values
        ugy = ry
        print("the coordinates are ({},{})".format(rx, ry))
        var_sig_pair_uv(n, v, px, py, a)
        vqx = rx #this rx and ry should be different that the above two aka why set to different var
        vqy = ry #because below plug them into point addition and need the four different values

        point_addition(n, a, ugx, ugy, vqx, vqy)
        rG = rx % n
        if r == rG:
            print("The signature valid!")
            sys.exit()
        else:
            print("The signature is not valid.")



def run_with_prompt():
    # print("Crypto Program")
    z = int(input("Please enter the data value: "))  # Data number #17
    n = int(input("Please enter the order: "))  # order #79
    a = int(input("Please enter the value for a: "))  # intercept ellipse equation #0
    px = int(input("Please enter the x coordinate of the base point: "))  # base point x point #2
    py = int(input("Please enter the y coordinate of the base point: "))  # base point y point #22
    qqx = int(input("Please enter the x coordinate of the public key: "))  # public key x point #52
    qqy = int(input("Please enter the y coordinate of the public key: "))  # public key y point #7
    r = int(input("Please enter the x coordinate of the signature: "))  # sig x point #62
    s = int(input("Please enter the y coordinate of the signature: "))  # sig y point #47

    verify_sig_pair(r, s, n, qqx, qqy, z, a, px, py)

def main():
    run_with_prompt()


if __name__ == "__main__":
    main()