from args import args
from Equation import Expression

# args = arg_parser.parse_args()

f = Expression(args.equation, ["x"])


def p(a: float, b: float) -> float:
    return b-((f(b)*(b-a))/(f(b)-f(a)))
