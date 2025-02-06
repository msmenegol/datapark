# DATAPARK

Datapark is a self-hosted data platform for educational purposes. It consists of a collection of containerized services that allow the user to build solutions for data-related problems. To use them, you'll need to have [docker](https://docs.docker.com/) installed. On the [docker-compose](docker-compose.yaml) file you can find the following services:

- [jupyterlab](https://jupyter.org/): a Jupyter lab server. This is where a developer should be able to use notebooks for handling their data and prototyping their solution.
- [postgresql](https://www.postgresql.org/): a PostgreSQL database. This can be used for storing data. It's used by other services to store their metadata, such as Minio and MLFlow.
- [minio](https://min.io/): a Minio storage service. It behaves similarly to S3 (AWS). This is the intended place for storing data.
- [mlflow](https://mlflow.org/): a MLFlow tracking server to support machine leraning tasks and applications.
- [spark](https://spark.apache.org/): the 3 Spark containers (one master and two workers) provide a Spark cluster that can be used for computing tasks.
- [airflow](https://airflow.apache.org/): the 3 Airflow containers (one for setting up, one for the web-ui, and one for the scheduler) allows for the scheduling and monitoring of data workflows.

To use, simply clone this repository.
To run everything (on a Unix/WSL terminal):
```shell
docker compose up -d
```

To shut it down:
```shell
docker compose down
```

To access the different services on the browser:
- jupyterlab: http://localhost:8888
- minio: http://localhost:9001
- mlflow: http://localhost:8080
- airflow: http://localhost:8081
- spark: http://localhost:9090

You can find usernames and password for the different services on the [.env](.env) file. I've had some issues with the terminal loading the variables in the .env file and then passing them on to `docker compose`, not allowing it to reload the contents of the file. Therefore, if you make changes to it, I suggest restarting the services from a fresh terminal. Please make sure you change those before using, especially the passwords.
The platform has examples to help you use the different services from notebooks. There is also an example on how to build Airflow DAGs that run on Spark.
By defaut, notebooks are stored on `platform/jupyterlab/notebooks/` and DAGs can be found on `platform/airflow/dags`.
