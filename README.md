# DATAPARK

Datapark is a self-hosted data platform for educational purposes. It consists of a collection of containerized services that allow for someone to build solutions for data-related problems. On the docker-compose file you can find the following services:

- jupyterlab: a jupyter lab server. This is where a developer should be able to use notebooks for handling their data and prototyping their solution.
- postgresql: a PostgreSQL database. This can be used for storing data. It's used by other services to store their metadata, such as Minio and MLFlow.
- minio: a Minio storage service. It behaves similarly to S3 (AWS). This is the intended place for storing data.
- mlflow: a MLFlow tracking server to support machine leraning tasks and applications.
- spark: the 3 Spark containers (one master and two workers) provide a Spark cluster that can be used for computing tasks.
- airflow: the 3 Airflow containers (one for setting up, one for the webui, and one for the scheduler) allows for the scheduling and monitoring of data workflows.
