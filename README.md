# DATAPARK

Datapark is a self-hosted data platform for educational purposes. It consists of a collection of containerized services that allow the user to build solutions for data-related problems. On the [docker-compose](docker-compose.yaml) file you can find the following services:

- [jupyterlab](https://jupyter.org/): a Jupyter lab server. This is where a developer should be able to use notebooks for handling their data and prototyping their solution.
- [postgresql](https://www.postgresql.org/): a PostgreSQL database. This can be used for storing data. It's used by other services to store their metadata, such as Minio and MLFlow.
- [minio](https://min.io/): a Minio storage service. It behaves similarly to S3 (AWS). This is the intended place for storing data.
- [mlflow](https://mlflow.org/): a MLFlow tracking server to support machine leraning tasks and applications.
- [spark](https://spark.apache.org/): the 3 Spark containers (one master and two workers) provide a Spark cluster that can be used for computing tasks.
- [airflow](https://airflow.apache.org/): the 3 Airflow containers (one for setting up, one for the webui, and one for the scheduler) allows for the scheduling and monitoring of data workflows.

To run everything:
```shell
docker compose up --attach jupyterlab
```

Attaching Jupyterlab will ensure that you get the URL with the token on the terminal and it doesn't get lost amidst other messages.

To access the different services on the browser:
- minio: http://localhost:9001
- mlflow: http://localhost:8080
- airflow: http://localhost:8081
- spark: http://localhost:9090

The platform has examples to help you use the different services from notebooks. There is also an example on how to build Airflow DAGs that run on Spark.
You can find usernames and password for the different services on the [.env](.env) file. Please make sure you change those before using.
