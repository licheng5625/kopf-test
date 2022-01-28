FROM python:3.7
RUN mkdir /src
ADD nats_operator.py /src
RUN pip install kopf


CMD kopf run /src/nats_operator.py --verbose
