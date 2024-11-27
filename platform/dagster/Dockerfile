FROM python:3.11.10-slim

# REINSTALL ALL PACKAGES FOR THIS PYTHON VERSION

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app /opt/dagster/logs

RUN pip install dagster-webserver dagster-postgres dagster-aws dagster-mlflow dagster-deltalake dagster-deltalake-pandas

ENV DAGSTER_HOME=/opt/dagster/dagster_home

COPY dagster.yaml /opt/dagster/dagster_home/

COPY repo.py workspace.yaml /opt/dagster/app/

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["/bin/bash"]
