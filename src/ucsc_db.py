import argparse
import sqlite3
import gzip
import time


bin_size = [128000, 1000000, 8000000, 64000000, 512000000]
bin_offset = [0,
              512000000//128000,
              512000000//128000 + 512000000//1000000,
              512000000//128000 + 512000000//1000000 + 512000000//8000000,
              512000000//128000 + 512000000//1000000 + 512000000//8000000 \
                      + 512000000//64000000]

def get_bin(start, end):
    ##############################
    # Your code here
    ##############################

    return target_bin

def get_query_bins(start, end):
    query_bins = []

    ##############################
    # Your code here
    ##############################

    return query_bins

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', type=str, required=True)
    parser.add_argument('-q', '--query', type=str, required=True)
    return parser.parse_args()

def create_and_connect_db(db_name='ucsc_genomic_intervals.db'):
    ##############################
    # Your code here
    ##############################

def insert_interval(chromosome, start, end, conn):
    ##############################
    # Your code here
    ##############################

def insert_interval_file(file_path, conn, ucsc=False):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            A = line.strip().split('\t')
            chromosome, start, end = A[:3]
            start, end = int(start), int(end)
            insert_interval(chromosome, start, end, conn)

def count_intersecting_intervals(chromosome, start, end, conn):
    ##############################
    # Your code here
    ##############################

def count_interval_file(file_path, conn):
    total = 0
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            A = line.strip().split('\t')
            chromosome, start, end = A[:3]
            start, end = int(start), int(end)
            total += count_intersecting_intervals(chromosome, start, end, conn)
    return total

def main():
    args = get_args()

    db_connection = create_and_connect_db()

    start_time = time.time()
    insert_interval_file(args.database, db_connection)
    end_time = time.time()
    print(f"DB insert time: {end_time - start_time}")

    start_time = time.time()
    count = count_interval_file(args.query, db_connection)
    end_time = time.time()
    print(f"DB query time: {end_time - start_time}")

    print(f"Total intersecting intervals: {count}")

if __name__ == '__main__':
    main()
