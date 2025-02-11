from math import pow, sqrt
from statistics import mean

def dE(one, two):
    return sqrt(
        sum([
            pow(0.001 * ((two[1] - one[1])/(pow(two[0] - one[0], 2))), 2),
            pow(0.001 * ((one[1] - two[1])/(pow(two[0] - one[0], 2))), 2),
            pow(0.01 * ((1)/(two[0] - one[0])), 2),            
            pow(0.01 * ((1)/(one[0] - two[0])), 2),
        ])
    )

d_one = (0, 7.05)
d_two = (0.5, 7.13)
d_three = (1.0, 7.25)
d_four = (1.5, 7.33)
d_five = (2.0, 7.45)

a = dE(d_one, d_two)
b = dE(d_two, d_three)
c = dE(d_three, d_four)
d = dE(d_four, d_five)

print(f"{a = }, {b = }, {c = }, {d = }")
print(f"{mean([a,b,c,d]) = }")