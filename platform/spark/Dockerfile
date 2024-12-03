FROM spark:3.5.3-scala2.12-java11-ubuntu

USER root
RUN echo root:rootpw | chpasswd
RUN echo spark:sparkpw | chpasswd

RUN set -ex; \
    echo "deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu focal main" >> /etc/apt/sources.list; \
    echo "deb-src https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu focal main" >> /etc/apt/sources.list; \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F23C5A6CF475977595C89F51BA6932366A755776; \
    apt-get update; \
    apt-get install -y python3.12-full; \
    ln -sfn /usr/bin/python3.12 /usr/bin/python3; \
    python3 -m ensurepip --default-pip; \
    rm -rf /var/lib/apt/lists/*;

USER spark
