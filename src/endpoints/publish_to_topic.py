from fastapi import APIRouter
from pyxi_kafka_client import KafkaProducerManager
from models.publish_req import PublishReq
from json import dumps as json_dumps

router = APIRouter()


def get_configuration() -> dict[str, str]:
    return {
        "bootstrap.servers": "localhost:9092",
    }


@router.post("/topic/publish")
async def publish_to_topic(req: PublishReq):
    # if not req.validate():
    #     print("Validation Errors:", req.errors())
    #     raise

    configuration = get_configuration()
    manager = KafkaProducerManager(req.topic).init(configuration)
    json_payload = json_dumps(req.payload)
    # manager.produce(req.key, req.payload)
    manager.produce(req.key, json_payload)
    manager.flush()

    return {"status": "accepted"}
