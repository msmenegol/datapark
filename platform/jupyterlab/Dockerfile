FROM python:3.12.5-slim

RUN useradd -ms /bin/bash jptr
USER jptr

WORKDIR /home/jptr
ENV PATH="/home/jptr/.local/bin:${PATH}"

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

RUN mkdir -p /home/jptr/app/

ENTRYPOINT ["/bin/bash"]
