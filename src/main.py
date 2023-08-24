from fastapi import FastAPI
from pyxi_kafka_client import KafkaProducerManager
from reqs import PublishReq
import asyncio

app = FastAPI()


@app.get("/kafka/topic/{topic_name}/consumer/configuration")
async def get_consumer_configuration(topic_name: str):
    pass


@app.post("/kafka/topic/{topic_name}/publish")
async def publish_to_topic(topic_name: str, req: PublishReq):
    manager = KafkaProducerManager(topic_name).init()
    manager.publish(req.key, req.payload)
    return {"status": "accepted"}


if __name__ == "__main__":

    async def main():
        pass

    asyncio.run(main())
