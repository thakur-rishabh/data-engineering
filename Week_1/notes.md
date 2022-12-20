# Postgres docker

1. Run docker container
    ```
    docker run -it \
        -e POSTGRES_USER="root" \
        -e POSTGRES_PASSWORD="root" \
        -e POSTGRES_DB="ny_taxi" \
        -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
        -p 5432:5432 \
        postgres:13
    ```

2. Install pgcli for interaction with postgres 
    - For windows `pip3 install pgcli`
    - For mac os: `brew install pgcli`

3. Connection through pgcli and postgres docker container `pgcli -h localhost -p 5432 -u root -d ny_taxi`

4. Data set for New york taxi data
    - Data set: [NY Taxi data for 2021](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet)
    - Data dictionary: [NY Taxi data dict](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)
