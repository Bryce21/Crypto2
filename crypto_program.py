if __name__ == "__main__":
    print("Crypto Program")

    import random

    z = int(input("Please enter the data value: ")) #Data number #17
    mod = int(input("Please enter the module divisor you would like to use: ")) #order #67
    n = int(input("Please enter the order: ")) #order #79
    d = int(input("Please enter the private Key: ")) #private key #2
    a = int(input("Please enter the value for a: ")) #intercept ellipse equation #0
    px = int(input("Please enter the x coordinate: ")) #base point x point #2
    py = int(input("Please enter the y coordinate: ")) #base point y point #22

    #c=0
    rx=0
    ry=0
    k = random.randint(1, n-1)
    #print(k) #print check to see fi this is odd or even, to see if this even go through if statement or odd go through else

def test_prime(n):
    if n == 1:
        return False
    elif n == 2 :
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
            return True
#print(test_prime(d))
#print(test_prime(mod))


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
    return rx, ry
#print("C is: {}, rx/ry is: ({}, {})".format(c, rx, ry))


def point_addition(mod, a, px, py, qx, qy):
    check = (qy - py) / (qx - px)
    # print(check)
    if not float(check).is_integer():
        den_inv = pow((qx - px), mod - 2, mod)
        c = ((qy - py) * den_inv) % mod
    else:
        c = check % mod
    rx = (c ** 2 - px - qx) % mod
    ry = (c * (px - rx) - py) % mod
    return rx, ry
#print("C is: {}, rx/ry is: ({}, {})".format(c, rx, ry))

if not test_prime(d): #testing to make sure that the private key is prime
    print("Please make sure all your numbers are entered correctly. (Some should be prime!)")
elif not test_prime(mod): #testing to make sure that the module is prime
    print("Please make sure all your numbers are entered correctly. (Some should be prime!)")
else:
    #print("hello")
   if k % 2 == 0:
       # even--point doubling k/2 amount of times
        i = k/2
        while i < k:
            rx, ry = point_doubling(mod, a, px, py) #these values that can't be found will be passed in from the user
            px=rx #trying to return rx and ry from the point_doubling method and then set back equal to px, py to pass the new values back into the method but cant seem to get it to work?? something to do with self.variables but I don't know how they work or how to use classes
            py=ry
            i = k-1
   else:
       # odd--(k-1)/2 point doubling amount of times then one point addition at the end
        i = (k-1) / 2
        while i < k:
            rx, ry = point_doubling(mod, a, px, py) #same issue as above but this one has to pass to point_addition method after it finishes going through point_doubling method an x amount of times...
            px=rx #same with return and self.variables?
            py=ry
            i = k-1
        # qx=px # px from point doubling method
        # qy=py # py from point doubling method
        # point_addition(mod, a, px, py, qx, qy) #not quite sure how this will work?..
        #                                 # qx and qy are the px and py values from the
        #                                 #prevous point_doubling method and px and py
        #                                 # will be the original values passed in from the user


r = rx % n
if r == 0:
    print("r=0 Please start again!")
else
    s= (z + r * d) / (k % n)
    if s == 0:
        print("s=0 Please start again!")
    else:
        print("The signature pair is ({},{})"..format(r, s))