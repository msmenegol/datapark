#!/bin/bash

psql -U ${POSTGRES_USER} <<-END
    create database ${MLFLOW_DB_USER};
    create user ${MLFLOW_DB_USER} with encrypted password '${MLFLOW_DB_PASSWORD}';
    alter database ${MLFLOW_DB_USER} owner to ${MLFLOW_DB_USER};
    grant all privileges on database ${MLFLOW_DB_USER} to ${MLFLOW_DB_USER};
END

psql -U ${POSTGRES_USER} <<-END
    create database ${AIRFLOW_DB_USER};
    create user ${AIRFLOW_DB_USER} with encrypted password '${AIRFLOW_DB_PASSWORD}';
    alter database ${AIRFLOW_DB_USER} owner to ${AIRFLOW_DB_USER};
    grant all privileges on database ${AIRFLOW_DB_USER} to ${AIRFLOW_DB_USER};
END
