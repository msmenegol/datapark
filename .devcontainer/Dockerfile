FROM python:3.12.5-slim

RUN apt-get -y update
RUN apt-get -y install git

RUN useradd -ms /bin/bash dev

USER dev
WORKDIR /home/dev

RUN pip install 'pre-commit==3.8.0'

ENTRYPOINT ["/bin/bash"]
