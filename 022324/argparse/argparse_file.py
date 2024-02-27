import argparse

parse = argparse.ArgumentParser(fromfile_prefix_chars='@')

parse.add_argument('-a')
parse.add_argument('-b')
parse.add_argument('-c')
parse.add_argument('-d')
parse.add_argument('-e')
parse.add_argument('-f')

args = parse.parse_args()

print(vars(args))