import argparse
from collections import namedtuple
import heapq
import gzip

Interval = namedtuple('Interval', ['chrm', 'start', 'end'])

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', type=str, required=True)
    parser.add_argument('-q', '--query', type=str, required=True)
    return parser.parse_args()

def read_interval_file(file):
    intervals = []
    with gzip.open(file, 'rt') as f:
        for line in f:
            A = line.strip().split('\t')
            interval = Interval(chrm=A[0], start=int(A[1]), end=int(A[2]))
            intervals.append(interval)
    intervals.sort(key=lambda x: (x.chrm, x.start, x.end))
    return intervals

def merge_intersect(A, B):
    ##############################
    # Your code here
    ##############################

def main():
    args = get_args()


    start_time = time.time()
    D = read_interval_file(args.database)
    Q = read_interval_file(args.query)
    end_time = time.time()
    print(f"Read and sort time: {end_time - start_time}")

    start_time = time.time()
    count = merge_intersect(Q, D)
    end_time = time.time()
    print(f"Query time: {end_time - start_time}")

    print(f"Total intersecting intervals: {count}")

if __name__ == '__main__':
    main()
