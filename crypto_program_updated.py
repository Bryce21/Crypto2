
import random
import sys

# def read_int(prompt):
#     return int(input(prompt))

def test_prime(n):
    if n == 1 :
        return False
    elif n == 2 :
        return True
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
            return True

def point_doubling(mod, a, px, py):
    check = ((3 * px ** 2) + a) / (2 * py)
    # print(check)
    if not float(check).is_integer():
        den_inv = pow((2 * py), mod - 2, mod)
        c = (((3 * px ** 2) + a) * den_inv) % mod
        # print(c)
    else:
        c = (((3 * px ** 2) + a) / (2 * py)) % mod
    new_rx = (c ** 2 - (2 * px)) % mod
    new_ry = (c * (px - new_rx) - py) % mod
    return { "rx": new_rx, "ry": new_ry }

def point_addition(mod, a, px, py, qx, qy):
    check = (qy - py) / (qx - px)

    if not float(check).is_integer():
        den_inv = pow((qx - px), mod - 2, mod) #finding the denominator inverse,
        #print(den_inv)
        c = ((qy - py) * den_inv) % mod
    else:
        c = check % mod
   
    new_rx = (c ** 2 - px - qx) % mod
    new_ry = (c * (px - new_rx) - py) % mod
    return { "rx": new_rx, "ry": new_ry }

def calculate_signature_pair(z, mod, n, d, a, px, py):
    k = random.randint(1, n-1)
    print("k = ", k) #print check to see fi this is odd or even, to see if this even go through if statement or odd go through else
    
    # Hard coding k = 3 to work with the article example
    #k = 3

    # These will be overwritten multiple times, and initially should be the first point
    rx = px
    ry = py

    if not test_prime(d): #testing to make sure that the private key is prime
        print("Please make sure all your numbers are entered correctly. (Some should be prime!)")
        sys.exit()
    elif not test_prime(mod): #testing to make sure that the module is prime
        print("Please make sure all your numbers are entered correctly. (Some should be prime!)")
        sys.exit()
    else:

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

    r = rx % n

    if r == 0:
        print("r=0 Please start again!")
        sys.exit()
    else:
        s = (z + r * d) / (k % n)
        if s == 0:
            print("s=0 Please start again!")
            sys.exit()
        else:
            print("The signature pair is ({},{})".format(r, s))


def run_with_prompt():

    #print("Crypto Program")
    z = int(input("Please enter the data value: ")) #Data number #17
    mod = int(input("Please enter the module divisor you would like to use: ")) #order #67
    n = int(input("Please enter the order: ")) #order #79
    d = int(input("Please enter the private Key: ")) #private key #2
    a = int(input("Please enter the value for a: ")) #intercept ellipse equation #0
    px = int(input("Please enter the x coordinate: ")) #base point x point #2
    py = int(input("Please enter the y coordinate: ")) #base point y point #22

    calculate_signature_pair(z, mod, n, d, a, px, py)



def main():
    run_with_prompt()

    
if __name__ == "__main__":
    main()