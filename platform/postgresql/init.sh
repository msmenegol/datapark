#!/bin/bash

psql -U ${POSTGRES_USER} <<-END
    create database ${MLFLOW_DB_USER};
    create user ${MLFLOW_DB_USER} with encrypted password '${MLFLOW_DB_PASSWORD}';
    alter database ${MLFLOW_DB_USER} owner to ${MLFLOW_DB_USER};
    grant all privileges on database ${MLFLOW_DB_USER} to ${MLFLOW_DB_USER};
END

psql -U ${POSTGRES_USER} <<-END
    create database ${DAGSTER_DB_USER};
    create user ${DAGSTER_DB_USER} with encrypted password '${DAGSTER_DB_PASSWORD}';
    alter database ${DAGSTER_DB_USER} owner to ${DAGSTER_DB_USER};
    grant all privileges on database ${DAGSTER_DB_USER} to ${DAGSTER_DB_USER};
END
