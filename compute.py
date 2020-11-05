import formula


def compute(a, b, x=0):
    x = formula.p(a, b)
    if (formula.f(a) * formula.f(x) > 0):
        a = x
    else:
        b = x

    return (a, b, x)
