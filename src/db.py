import argparse
import sqlite3
import gzip
import time

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', type=str, required=True)
    parser.add_argument('-q', '--query', type=str, required=True)
    return parser.parse_args()

def create_and_connect_db(db_name='genomic_intervals.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS intervals")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS intervals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chromosome TEXT NOT NULL,
            start INTEGER NOT NULL,
            end INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE INDEX index_intervals ON intervals (chromosome, start, end)
    """)
    conn.commit()
    return conn

def insert_interval(chromosome, start, end, conn):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO intervals ' \
                   + '(chromosome, start, end) VALUES (?, ?, ?)',
                   (chromosome, start, end))
    conn.commit()
    return cursor.lastrowid

def insert_interval_file(file_path, conn):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            A = line.strip().split('\t')
            chromosome, start, end = A[:3]
            insert_interval(chromosome, start, end, conn)

def count_intersecting_intervals(chromosome, start, end, conn):
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM intervals
        WHERE chromosome = ? AND start <= ? AND end >= ?
    """
    cursor.execute(query, (chromosome, end, start))
    results = cursor.fetchall()
    #print(results)
    return len(results)

def count_interval_file(file_path, conn):
    total = 0
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            A = line.strip().split('\t')
            chromosome, start, end = A[:3]
            r = count_intersecting_intervals(chromosome, start, end, conn)
            #print(f"Chromosome: {chromosome}, Start: {start}, End: {end}, Count: {r}")
            #break
            total += r
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
