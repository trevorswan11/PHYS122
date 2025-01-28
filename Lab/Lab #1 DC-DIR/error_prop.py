from math import sqrt, pow

def experimental_sum(v, v_err, i, i_err):
    return sqrt(sum([
        pow(v_err / i, 2),
        pow((i_err * v) / pow(i, 2), 2)
    ]))
    
r1 = experimental_sum(2.55, 0.01, 0.0258, 0.0001)
r2 = experimental_sum(2.64, 0.01, 0.0133, 0.0001)
r3 = experimental_sum(2.7, 0.01, 0.0023, 0.0001)
r4 = experimental_sum(2.7, 0.01, 0.0022, 0.0001)
print("actual series equiv:", f"{r1 = }, {r2 = }, {r3 = }, {r4 = }")

def parallel_equiv(r1, r1_err, r2, r2_err, r3, r3_err, r4, r4_err, n):
    frac: function = lambda x, y: x / y
    s: function = lambda x: pow(x, 2)
    match n:
        case 2:
            return sqrt(sum([
                pow(r1_err * frac(s(r2), s(r1 + r2)), 2),
                pow(r2_err * frac(s(r1), s(r1 + r2)), 2)
            ]))
        case 3:
            return sqrt(sum([
                pow(r1_err * frac(s(r2) * s(r3), s(r1 * (r2 + r3) + r2 * r3)), 2),
                pow(r2_err * frac(s(r1) * s(r3), s(r1 * (r2 + r3) + r2 * r3)), 2),
                pow(r3_err * frac(s(r2) * s(r1), s(r1 * (r2 + r3) + r2 * r3)), 2)
            ]))
        case 4:
            return sqrt(sum([
                pow(r1_err * frac(1, s(r1) * s(frac(1, r1) + frac(1, r2) + frac(1, r3) + frac(1, r4))), 2),
                pow(r2_err * frac(1, s(r2) * s(frac(1, r1) + frac(1, r2) + frac(1, r3) + frac(1, r4))), 2),
                pow(r3_err * frac(1, s(r3) * s(frac(1, r1) + frac(1, r2) + frac(1, r3) + frac(1, r4))), 2),
                pow(r4_err * frac(1, s(r4) * s(frac(1, r1) + frac(1, r2) + frac(1, r3) + frac(1, r4))), 2)
            ]))

tot2 = parallel_equiv(99, 0.1, 99.2, 0.1, 980, 10, 48.4, 0.1, 2)
tot3 = parallel_equiv(99, 0.1, 99.2, 0.1, 980, 10, 48.4, 0.1, 3)
tot4 = parallel_equiv(99, 0.1, 99.2, 0.1, 980, 10, 48.4, 0.1, 4)
print("theoretical parallel equiv:", f"{tot2 = }, {tot3 = }, {tot4 = }")

r1 = experimental_sum(2.56, 0.01, 0.0260, 0.0001)
r2 = experimental_sum(2.40, 0.01, 0.0240, 0.0001)
r3 = experimental_sum(2.5, 0.1, 0.0511, 0.0001)
r4 = experimental_sum(2.3, 0.1, 0.0908, 0.0001)
print("actual parallel equiv:", f"{r1 = }, {r2 = }, {r3 = }, {r4 = }")