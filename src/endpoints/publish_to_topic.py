from fastapi import APIRouter
from pyxi_kafka_client import KafkaProducerManager
from models.publish_req import PublishReq

router = APIRouter()


def get_configuration() -> dict[str, str]:
    return {
        "bootstrap.servers": "localhost:9092",
    }


@router.post("/topic/{topic_name}/publish")
async def publish_to_topic(topic_name: str, req: PublishReq):
    configuration = get_configuration()
    print(f"topic: {topic_name}, key: {req.key}, payload: {req.payload}")
    manager = KafkaProducerManager(topic_name).init(configuration)
    manager.produce(req.key, req.payload)
    manager.flush()
    return {"status": "accepted"}
