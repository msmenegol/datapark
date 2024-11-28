FROM spark:3.5.3-scala2.12-java11-ubuntu

USER root
RUN echo root:rootpw | chpasswd
RUN echo spark:sparkpw | chpasswd

#RUN set -ex; \
#    apt-get update; \
#    apt install -y software-properties-common; \
#    add-apt-repository ppa:deadsnakes/ppa -y; \
#    apt-get install -y python3.12; \
#    ln -sfn /usr/bin/python3.12 /usr/bin/python3; \
#    apt-get install -y python3-pip; \
#    rm -rf /var/lib/apt/lists/*

USER spark
