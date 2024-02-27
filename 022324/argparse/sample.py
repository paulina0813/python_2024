import argparse

parse = argparse.ArgumentParser()

parse.add_argument('--list', type=str, nargs='+')
args = parse.parse_args()
print(args.list)