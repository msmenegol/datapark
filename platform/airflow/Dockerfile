FROM apache/airflow:2.10.3
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

USER root

RUN mkdir -p /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins
RUN rm /requirements.txt

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

USER airflow
