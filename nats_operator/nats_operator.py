import kopf



@kopf.on.create('natsexamples')
def create_nats_account(body,logger, **_):
    logger.info(f"creating nats account! ")
    kopf.event(body, type="Created", reason="SomeReason", message="Some message")

    return {'name': "nats account"}



@kopf.on.event('natsexamples')
def create_pod(event,logger, **_):
    logger.info(f"nats is created! ")
    logger.info(f"step 3: Creating a pod!! ")

    logger.error(event)