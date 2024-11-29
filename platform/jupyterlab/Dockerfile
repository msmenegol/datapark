FROM python:3.12.5-slim

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get install -y wget && \
    apt-get clean;

ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

RUN wget https://jdbc.postgresql.org/download/postgresql-42.7.2.jar
RUN wget https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
RUN wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
RUN mkdir -p /opt/spark_jars/
RUN mv postgresql-42.7.2.jar /opt/spark_jars/
RUN mv delta-spark_2.12-3.2.0.jar /opt/spark_jars/
RUN mv hadoop-aws-3.3.4.jar /opt/spark_jars/
RUN mv aws-java-sdk-bundle-1.12.262.jar /opt/spark_jars/

RUN echo root:rootpw | chpasswd

RUN useradd -ms /bin/bash jptr
RUN echo jptr:jptrpw | chpasswd
USER jptr

WORKDIR /home/jptr
ENV PATH="/home/jptr/.local/bin:${PATH}"

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

RUN mkdir -p /home/jptr/app/

ENTRYPOINT ["/bin/bash"]
