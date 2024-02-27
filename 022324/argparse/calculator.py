import argparse

parse = argparse.ArgumentParser(description="It's a calculator that allows you to add, substract, and multiply two numbers")
parse.add_argument('-num_one', '--number_one', type=int, help='This is parameter one')
parse.add_argument('-num_two', '--number_two', type=int, help='This is parameter two')

parse.add_argument(
    '-operation', '-operation',
    type=str,
    choices=['sum', 'substraction', 'multiplication'],
    default='sum',
    required=False,
    help='Selected operation for entered numbers'
    )

args = parse.parse_args()

if args.operation == 'sum':
    print(args.number_one + args.number_two)
elif args.operation == 'substraction':
    print(args.num_one - args.num_two)
elif args.operation == 'multiplication':
    print(args.num_one * args.num_two)