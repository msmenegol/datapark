FROM apache/airflow:2.10.3
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
USER root
RUN mkdir -p /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins
RUN rm /requirements.txt
USER airflow
