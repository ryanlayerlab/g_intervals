#!/usr/bin/env python
import random
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description="Reservoir Sampling")
    parser.add_argument("N", type=int, help="Number of samples to keep")
    return parser.parse_args()

def main():
    args = get_args()
    N = args.N
    S = []
    i = 0
    for line in sys.stdin:
        if i < N:
            S.append(line)
        else:
            j = random.randint(0,i)
            if j < N:
                S[j] = line
        i += 1

    for line in S:
        print(line.rstrip())

if __name__ == "__main__":
    main()
