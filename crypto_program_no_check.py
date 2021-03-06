import random
import sys


def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
            return True


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
    return {new_rx, new_ry}



def point_addition(mod, a, px, py, qx, qy):
    check = (qy - py) / (qx - px)

    if not float(check).is_integer():
        den_inv = pow((qx - px), mod - 2, mod)
        c = ((qy - py) * den_inv) % mod
    else:
        c = check % mod

    new_rx = (c ** 2 - px - qx) % mod
    new_ry = (c * (px - new_rx) - py) % mod
    return {new_rx, new_ry}



def calculate_signature_pair(z, mod, n, d, a, px, py):
    k = random.randint(1, n - 1)
    print("k = ", k)  # print check to see if this is odd or even, to see if this even go through if statement or odd go through else

    # Hard coding k = 3 to work with the article example
    #k = 3

    # These will be overwritten multiple times, and initially should be the first point
    rx = px
    ry = py

    if not test_prime(d):  # testing to make sure that the private key is prime
        print("Please make sure all your numbers are entered correctly. (Some should be prime!)")
        sys.exit()
    elif not test_prime(mod):  # testing to make sure that the module is prime
        print("Please make sure all your numbers are entered correctly. (Some should be prime!)")
        sys.exit()
    else:

        # When converting a float to an int, python automatically rounds a decimal down.
        num_multiplication = int(k / 2)

        # Each time a doubling is done, replace the current point with the newly calculated value
        for i in range(num_multiplication):
            rx, ry = point_doubling(mod, a, rx, ry)


            # Only need to add points when k >= 3 and is odd. In other cases, doubling will be enough
        if (k % 2 == 1) and k > 2:
            rx, ry = point_addition(mod, a, px, py, rx, ry)


    r = rx % n
    #print("the value of r is: {}".format(r))

    if r == 0:
        print("r=0 Please start again!")
        sys.exit()
    else:
        s_check = ((z + r * d) / k)
        if not float(s_check).is_integer():
            k_inv = pow(k, mod - 2, mod)
            s = ((z + r * d) * k_inv) % n
            s= int(s)
            if s == 0:
                print("s=0 Please start again!")
                sys.exit()
            else:
                print("The signature pair is ({},{})".format(r, s))
                print("The signature pair in hexadecimal form is ({},{})".format(hex(r), hex(s)))
        else:
            s = ((z + r * d) / k) % n
            s= int(s)
            if s == 0:
                print("s=0 Please start again!")
                sys.exit()
            else:
                print("The signature pair is ({},{})".format(r, s))
                print("The signature pair in hexadecimal form is ({},{})".format(hex(r), hex(s)))
    return {r, s}




def main():
    z = int(input("Please enter the data value: "))  # Data number #17
    mod = int(input("Please enter the module divisor you would like to use: "))  # order #67
    n = int(input("Please enter the order: "))  # order #79
    d = int(input("Please enter the private Key: "))  # private key #2
    a = int(input("Please enter the value for a: "))  # intercept ellipse equation #0
    px = int(input("Please enter the x coordinate of the base point: "))  # base point x point #2
    py = int(input("Please enter the y coordinate of the base point: "))  # base point y point #22

    calculate_signature_pair(z, mod, n, d, a, px, py)



if __name__ == "__main__":
    main()