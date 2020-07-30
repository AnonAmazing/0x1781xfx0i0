##import _xxqazwerty
import random as r

def x():
    az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    A = r.choice(az)
    B = r.choice(az)
    C = r.choice(az)
    D = r.choice(az)
    E = r.choice(num)
    F = r.choice(num)
    G = r.choice(num)
    H = r.choice(num)
    I = r.choice(num)
    opt = '<hex at 0x%s%s%s%s%s%s%s%s%s0>' % (E, F, G, H, A, B, C, I, D)
    X = opt
    return X
