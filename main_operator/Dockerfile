FROM python:3.7
RUN mkdir /src
ADD operator.py /src
ADD nats_obj.yaml /src
RUN pip install kopf
RUN pip install kubernetes
RUN pip install pyYaml
CMD kopf run /src/operator.py --verbose
