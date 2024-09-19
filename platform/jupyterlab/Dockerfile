FROM python:3.12.5-slim

RUN useradd -ms /bin/bash jptr

USER jptr
WORKDIR /home/jptr
ENV PATH="/home/jptr/.local/bin:${PATH}"

SHELL ["/bin/bash", "-c"]
ENV SHELL="/bin/bash"

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

ENTRYPOINT ["/bin/bash"]
#ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0"]
