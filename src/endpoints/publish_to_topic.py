from fastapi import APIRouter
from pyxi_kafka_client import KafkaProducerManager
from models.publish_req import PublishReq

router = APIRouter()


@router.post("/topic/{topic_name}/publish")
async def publish_to_topic(topic_name: str, req: PublishReq):
    manager = KafkaProducerManager(topic_name).init()
    manager.publish(req.key, req.payload)
    return {"status": "accepted"}
