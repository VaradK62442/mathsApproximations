# function to generate the n-th telephone number
# the n-th telephone number is defined to be the number of pairwise connections
# that can be made between n people

# T(n) = T(n-1) + (n-1) * T(n-2)
# T(0) = T(1) = 1

tele_dict = {
    0: 1,
    1: 1
}


def T(n):
    if n in tele_dict:
        return tele_dict[n]
    
    new_val = T(n-1) + (n-1) * T(n-2)
    tele_dict[n] = new_val
    return new_val


def test(fn, params):
    for elt in params:
        print(f"{elt}: {fn(elt)}")


test(T, [0, 1, 5, 10, 100, 20, 50, 1_000])