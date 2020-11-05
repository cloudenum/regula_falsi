from compute import compute
from args import args
from formula import f


def display_iteration(i, a, b, x):
    if (args.verbose):
        print(f"Iteration {i}")
        print(f"f({a}) = {f(a)}")
        print(f"f({b}) = {f(b)}")
        print(f"p = {x}")
        print()


try:
    f(1)
except TypeError:
    print(f"error: {args.equation} is not a valid equation")
    exit(1)

(a, b, x) = compute(args.a, args.b)
i = 1
display_iteration(i, args.a, args.b, x)
i = i + 1

while round(f(x), args.precision) != 0:
    (a, b, x) = compute(a, b, x)
    display_iteration(i, a, b, x)
    i = i + 1

print(f"{x} aprroximately equal to {round(x, args.precision)}")
