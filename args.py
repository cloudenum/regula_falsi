import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("equation", type=str,
                        metavar="equation", help="The root equation. Use quote, if error happened.")
arg_parser.add_argument("-a", "-x0", help="The a or x0 value. Default = 1",
                        type=float, default=1)
arg_parser.add_argument("-b", "-x1", help="The b or x1 value. Default = 2",
                        type=float, default=2)
arg_parser.add_argument("--precision", type=int,
                        help="""Specify the decimal precision used for rounding the root value in every iteration.
                    Default = 4""", default=4)
arg_parser.add_argument("-v", "--verbose",
                        help="Output every iteration. This will compute every iteration twice.", action="store_true")

args = arg_parser.parse_args()
