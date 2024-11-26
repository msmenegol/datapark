FROM python:3.12.5-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app /opt/dagster/logs

RUN pip install dagster-webserver dagster-postgres dagster-aws dagster-mlflow

ENV DAGSTER_HOME=/opt/dagster/dagster_home

COPY dagster.yaml /opt/dagster/dagster_home/

COPY repo.py workspace.yaml /opt/dagster/app/

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["/bin/bash"]
