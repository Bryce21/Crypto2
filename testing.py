def run_with_prompt():
    x=12
    y=13
    z=14

    n_point_doubling(x, y, z)

def n_point_doubling(x, y, w):
    t= x+y+w
    print("the value is {} {}".format(t, w))


def main():
    run_with_prompt()


if __name__ == "__main__":
    main()