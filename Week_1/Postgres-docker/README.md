# Postgres docker
1. Create docker network `docker network create pg-network`

2. Run docker container
    ```
    docker run -it \
        -e POSTGRES_USER="root" \
        -e POSTGRES_PASSWORD="root" \
        -e POSTGRES_DB="ny_taxi" \
        -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
        -p 5432:5432 \
        --network=pg-network \
        --name pg-databse \
        postgres:13
    ```

3. Install pgcli for interaction with postgres 
    - For windows `pip3 install pgcli`
    - For mac os: `brew install pgcli`

4. Connection through pgcli and postgres docker container `pgcli -h localhost -p 5432 -u root -d ny_taxi`

5. Data set for New york taxi data
    - Data set: [NY Taxi data for 2021](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet)
    - Data dictionary: [NY Taxi data dict](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

6. PGAdmin docker
    ```
    docker run -it \
        -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
        -e PGADMIN_DEFAULT_PASSWORD="root" \
        -p 8080:80 \
        --network=pg-network \
        --name pgadmin \
        dpage/pgadmin4
    ```

7. Ingest data to postgres
    ```
    python3 ingest_data.py \
        --user=root \
        --password=root \
        --host=localhost \
        --port=5432 \
        --db=ny_taxi \
        --table-name=yellow_taxi_trips \
        --url=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
    ```

8. Dockerizing ingestion:
    -  Create Dockerfile
    -  Build image `docker build -t taxi_ingest:1.0 .`
    -  Run below:
       ```
        docker run -it \
            --network=pg-network \
            taxi_ingest:1.0 \
                   --user=root \
                    --password=root \
                    --host=pg-databse \
                    --port=5432 \
                    --db=ny_taxi \
                    --table-name=yellow_taxi_trips \
                    --url=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
       ```
