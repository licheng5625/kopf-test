import kopf
import kubernetes

import yaml
import os


@kopf.on.create('kopfexamples')
def create_nats(status, logger, **_):
    if not status.get('create_blob_storge', {}):
        raise kopf.TemporaryError("blob storge is not created yet.", delay=10)
    logger.info(status.get('create_blob_storge', {})["name"] +" is created  "  )
    logger.info(f"step 2: Creating nats! ")

    # path = os.path.join(os.path.dirname(__file__), 'nats_obj.yaml')
    # tmpl = open(path, 'rt').read()
    # text = tmpl.format(name= "nats-example-1")
    # data = yaml.safe_load(text)
    # my_resouces = {
    #     "apiVersion": "kopf.dev/v1",
    #     "kind": "NatsExample",
    #      "name": "nats-example-1"
    # }
    # K8s(configuration_json=cls)
    # api = kubernetes.client.CustomObjectsApi()
    # obj = api.create_cluster_custom_object(
    #      group='kopf.dev',
    #      body=my_resouces,
    #      version='v1',
    #      plural='natsexamples'
    # )

    return {'name': "nats"}

@kopf.on.create('kopfexamples')
def create_blob_storge(logger, **_):
    logger.info(f"step 1: upload blob! ")
    return {'name': "my_blob"}


@kopf.on.event('natsexamples')
def create_pod(event,logger, **_):
    logger.info(f"nats is created! ")

    logger.error(event)

 

@kopf.on.delete('kopfexamples')
def delete(logger, **kwargs):
    logger.info(f"deleting resource! ")


path = os.path.join(os.path.dirname(__file__), 'nats_obj.yaml')
tmpl = open(path, 'rt').read()
text = tmpl.format(name= "nats-example-1")
data = yaml.safe_load(text)
api = kubernetes.client.CustomObjectsApi()
obj = api.create_cluster_custom_object(
     group='kopf.dev',
     body=data,
     version='v1',
     plural='natsexamples'
)