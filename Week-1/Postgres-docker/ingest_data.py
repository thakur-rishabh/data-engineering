#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    # command line arguments
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # dataset name
    parquet_name = 'output.parquet'
    csv_name = 'output.csv'

    # downloading
    os.system(f"wget {url} -O {parquet_name}")

    # create connection with postgresql container
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # loading parquet based data & convert to csv
    df = pd.read_parquet(parquet_name)
    df.to_csv(csv_name)

    # creating chunks
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    # fix type for pickup and dropoff time
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # initial heading sent to postgres instance
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()
            df = next(df_iter)

            # fix type for pickup and dropoff time
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            # sending to postgres instance
            df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()
            print('inserted another chunk, took %.3f second' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insert CSV data to Postgres')
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='databse name for postgres')
    parser.add_argument('--table-name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the parquet file')
    args = parser.parse_args()

    # main function calling
    main(args)