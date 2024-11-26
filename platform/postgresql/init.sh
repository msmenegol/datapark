#!/bin/bash

psql -U ${POSTGRES_USER} <<-END
    create database ${MLFLOW_DB_USER};
    create user ${MLFLOW_DB_USER} with encrypted password '${MLFLOW_DB_PASSWORD}';
    alter database mlflow owner to ${MLFLOW_DB_USER};
    grant all privileges on database mlflow to ${MLFLOW_DB_USER};
END
