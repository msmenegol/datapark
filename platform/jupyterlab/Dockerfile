FROM python:3.12.5-slim

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

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
